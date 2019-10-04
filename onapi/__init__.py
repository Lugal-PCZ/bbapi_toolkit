from pathlib import Path as _Path
import sys as _sys
import configparser as _configparser
import requests as _requests

from . import academics
from . import admissions
from . import athletics
from . import constituents
from . import content
from . import list
from . import school_info
from . import unpublished
from . import extras


class Client:
    def __init__(self, configfile: str) -> None:
        configfile = _Path(configfile)
        if configfile.exists():
            CONFIG = _configparser.RawConfigParser()
            CONFIG.read(configfile)
            self.urlbase = CONFIG['ON_API']['urlbase']
            auth = {'username': CONFIG['ON_API']['username'], 'password': CONFIG['ON_API']['password']}
            self.agent = {'User-agent': CONFIG['ON_API']['agent']}
            r = _requests.post(
                f'{self.urlbase}/authentication/login',
                data=auth,
                headers=self.agent,
            )
            self.token = r.json()['Token']
        else:
            print()
            _sys.tracebacklimit = 0
            raise FileNotFoundError(f'\nThe config file ({configfile}) couldn’t be found.\nPlease copy the config.ini.example file to your project directory and fill out the appropriate ON API settings for this project.\n')
