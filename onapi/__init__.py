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
    """Object which creates the connection to the Blackbaud ON API
    and stores attributes which are needed to query the API endpoints.

    Args:
        configfile (str): The name of the configuration file for this client.

    Attributes:
        urlbase (str): The base URL for all the API endpoints. Read from the config file.
        agent (str): The http User-agent header that this script will run as. Read from the config file.
        token (str): The ON API token, which is acquired in __init()__.
    """
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
                message = eval(f.read())
            _sys.tracebacklimit = 0
            raise FileNotFoundError(message)
