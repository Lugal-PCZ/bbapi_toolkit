# Note these are UNPUBLISHED endpoints. Though they may be useful, they cannot be relied
# upon for production purposes, and Blackbaud may change or restrict them without warning.

from .. import requests
from .. import urlbase
from .. import agent
from .. import token


def get_rooms() -> list:
    """Get buildings and rooms.

    Returns:
        List of dictionaries.
    """
    r = requests.get('{}/venue/buildinglist'.format(urlbase), params={'t': token}, headers=agent)
    return r.json()
