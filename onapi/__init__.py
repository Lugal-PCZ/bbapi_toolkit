import requests

from .. import CONFIG

urlbase = CONFIG['ON_API']['urlbase']
agent = {'User-agent': CONFIG['ON_API']['agent']}
auth = {'username': CONFIG['ON_API']['username'], 'password': CONFIG['ON_API']['password']}
r = requests.post('{}/authentication/login'.format(urlbase), data=auth, headers=agent)
token = r.json()['Token']

# Import ON API endpoints
# See https://docs.blackbaud.com/on-api-docs/api for documentation of the ON API endpoints.
from .endpoints import academics
from .endpoints import admissions
from .endpoints import athletics
from .endpoints import constituents
from .endpoints import content
from .endpoints import list
from .endpoints import school_info

# Import unpublished ON API endpoints
from .endpoints import unpublished_endpoints

# Import Extra functions that leverage the ON API
from . import extras

