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
            config = _configparser.RawConfigParser()
            config.read(configfile)
            self.urlbase = config['ON_API']['urlbase']
            auth = {'username': config['ON_API']['username'], 'password': config['ON_API']['password']}
            self.agent = {'User-agent': config['ON_API']['agent']}
            r = _requests.post(
                f'{self.urlbase}/authentication/login',
                data=auth,
                headers=self.agent,
            )
            self.token = r.json()['Token']
        else:
            print()
            with open(f'{_Path(__file__).parent.parent}/config.ini.example', 'r') as f:
                example = f.read()
            message = (
                '\n\n'
                f'The specified config file ({configfile}) couldn’t be found. Copy the\n'
                f'config.ini.example file (below) to your project directory and fill\n'
                f'out the appropriate ON API settings for this project.\n\n'
                f'---------------------- config.ini.example ----------------------\n\n'
                f'{example}\n'
                f'----------------------------------------------------------------\n'
            )
            _sys.tracebacklimit = 0
            raise FileNotFoundError(message)
