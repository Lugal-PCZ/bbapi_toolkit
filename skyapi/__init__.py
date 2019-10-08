from pathlib import Path as _Path
import os as _os
import sys as _sys
import configparser as _configparser
import datetime as _datetime
import pickle as _pickle
from requests_oauthlib import OAuth2Session as _OAuth2Session
import time as _time

# from . import academics
# from . import admissions
# from . import athletics
# from . import constituents
# from . import content
# from . import list
# from . import school_info
# from . import unpublished
# from . import extras


class Client:
    """Object which creates the connection to the Blackbaud SKY API
    and stores attributes which are needed to query the API endpoints.

    Args:
        configfile (str): The name of the configuration file for this client.
        schoolyear (str): The school year that will be queried (in the format
            of '2019-2020'). Defaults to the current school year.

    Attributes:
        headers (dict): User agent and API subscription key, which are used
            for queries against API endpoints.
        schoolyear (str): The school year, which is used for some API
            endpoint queries.
        session (obj): OAuth2Session object.
    """
    def __init__(self, configfile: str, schoolyear: str = None) -> None:
        configfile = _Path(configfile)
        if configfile.exists():
            config = _configparser.RawConfigParser()
            config.read(configfile)
            self._rate_limit_timer = _datetime.datetime.now()
            self.headers = {
                'User-agent': config['SKY_API']['agent'],
                'Bb-Api-Subscription-Key': config['SKY_API']['subscription_key'],
            }
            self._account = config['SKY_API']['account']
            # Note that what in Blackbaud's nomenclature are "Application ID" and "Application Secret"
            # are "client_id" and "client_secret," respectively, for Requests-OAuthlib.
            self._client_id = config['SKY_API']['application_id']
            self._client_secret = config['SKY_API']['application_secret']
            self._redirect_uri = config['SKY_API']['redirect_uri']
            self._queries_per_second = config['SKY_API']['queries_per_second']
            self.session = _OAuth2Session(
                self._client_id,
                redirect_uri=self._redirect_uri,
                scope=[],
                auto_refresh_url='https://oauth2.sky.blackbaud.com/token',
                auto_refresh_kwargs={
                    'client_id': self._client_id,
                    'client_secret': self._client_secret,
                },
                token_updater=self._save_token,
            )
            if not self._check_if_token_exists():
                self._new_login()
            else:
                self.session.token = self._token
            self.schoolyear = schoolyear
            if not schoolyear:
                self.schoolyear = self._get_current_school_year()
        else:
            print()
            with open(f'{_Path(__file__).parent.parent}/config.ini.example', 'r') as f:
                message = eval(f.read())
            _sys.tracebacklimit = 0
            raise FileNotFoundError(message)


    def _check_if_token_exists(self) -> bool:
        exists = False
        try:
            with open(f'skyapitokens/{self._account}', 'rb') as f:
                exists = True
                self._token = _pickle.load(f)
        except:
            exists = False
        return exists


    def _new_login(self) -> bool:
        authorization_url, state = self.session.authorization_url('https://oauth2.sky.blackbaud.com/authorization')
        print('---------- USER AUTHORIZATION REQUIRED ----------')
        print(f'Please go to {authorization_url}')
        print(f'Log in as {self._account}, and authorize access.')
        authorization_response = input('Then enter the full callback URL: ')
        try:
            self._token = self.session.fetch_token(
                'https://oauth2.sky.blackbaud.com/token',
                authorization_response=authorization_response,
                client_secret=self._client_secret
            )
            self._save_token(self._token)
            print('\nSuccessfully authorized.')
        except:
            print('\nAuthorization failed.')


    def _save_token(self, token: dict) -> None:
        _os.makedirs('skyapitokens', exist_ok=True)
        with open(f'skyapitokens/{self._account}', 'wb') as f:
            _pickle.dump(token, f)


    def rate_limiter(self) -> None:
        interval = 1/int(self._queries_per_second)
        delta = (_datetime.datetime.now() - self._rate_limit_timer).seconds
        fudgefactor = 0.1
        if delta > interval:
            self._rate_limit_timer = _datetime.datetime.now()
        else:
            _time.sleep(interval - delta + fudgefactor)
            self._rate_limit_timer = _datetime.datetime.now()


    def _get_current_school_year(self) -> str:
        self.rate_limiter()
        r = self.session.get(
            'https://api.sky.blackbaud.com/school/v1/years',
            headers=self.headers
        )
        for each_row in r.json()['value']:
            if each_row['current_year'] == True:
                current_year = each_row['school_year_label']
                break
        return current_year
