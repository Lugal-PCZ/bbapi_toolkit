from pathlib import Path as _Path
import os as _os
import sys as _sys
import configparser as _configparser
import datetime as _datetime
import pickle as _pickle
from requests_oauthlib import OAuth2Session as _OAuth2Session
import hashlib as _hashlib
import time as _time

from . import accounts_payable
from . import communication_preference
from . import constituent
from . import fundraising
from . import general_ledger
from . import gift
from . import opportunity
from . import payments
from . import school
from . import statistical_unit
from . import treasury
from . import unpublished
from . import extras


class Client:
    """Object which creates the connection to the Blackbaud SKY API
    and stores attributes which are needed to query the API endpoints.

    Args:
        configfile (str): The name of the configuration file for this client.

    Attributes:
        headers (dict): User agent and API subscription key, which are used
            for queries against API endpoints.
        session (obj): OAuth2Session object.
    """
    def __init__(self, configfile: str = None) -> None:
        _sys.tracebacklimit = 0
        configerror = False
        if not configfile:
            configerror = True
            errormessage = 'No config file specified.\n\n'
        else:
            configfile = _Path(configfile)
            if configfile.exists():
                config = _configparser.RawConfigParser()
                try:
                    config.read(configfile)
                    self._rate_limit_timer = _datetime.datetime.now()
                    self.headers = {
                        'User-agent': config['SKY_API']['agent'],
                        'Bb-Api-Subscription-Key': config['SKY_API']['subscription_key'],
                    }
                    self._account = config['SKY_API']['account']
                    self._tokenfile = _hashlib.md5(f'{configfile}{self._account}'.encode('utf-8')).hexdigest()
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
                        # TODO: Handle expired tokens by calling _new_login()
                        self.session.token = self._token
                except:
                    configerror = True
                    errormessage = f'The specified config file (“{configfile}”) is not formatted correctly.\n\n'
            else:
                configerror = True
                errormessage = f'The specified config file (“{configfile}”) does not exist.\n\n'
        if configerror:
            print('\nERROR:')
            with open(f'{_Path(__file__).parent.parent}/config.ini.example', 'r') as f:
                errormessage += f.read()
            print(errormessage)


    def _check_if_token_exists(self) -> bool:
        exists = False
        try:
            with open(f'skyapitokens/{self._tokenfile}', 'rb') as f:
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
        with open(f'skyapitokens/{self._tokenfile}', 'wb') as f:
            _pickle.dump(token, f)


    def _rate_limiter(self) -> None:
        interval = 1/int(self._queries_per_second)
        delta = (_datetime.datetime.now() - self._rate_limit_timer).seconds
        fudgefactor = 0.01
        if delta > interval:
            self._rate_limit_timer = _datetime.datetime.now()
        else:
            _time.sleep(interval - delta + fudgefactor)
            self._rate_limit_timer = _datetime.datetime.now()


    def get(self, url: str, params: dict = {}) -> dict:
        self._rate_limiter()
        r = self.session.get(
            url,
            params=params,
            headers=self.headers,
        )
        return r.json()

    def post(self, url: str, params: dict) -> dict:
        self._rate_limiter()
        r = self.session.post(
            url,
            json=params,
            headers=self.headers,
        )
        return r.json()
