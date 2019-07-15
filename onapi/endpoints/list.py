from .. import requests
from .. import urlbase
from .. import agent
from .. import token



def get_list(listID: int) -> list:
    """Get data from a pre-built Blackbaud list.

    Documentation:
        https://docs.blackbaud.com/on-api-docs/api/list/get-list-id

    Args:
        listID (int): The Blackbaud ID for the requested list.

    Returns:
        List of dictionaries.
    """
    r = requests.get('{}/list/{}'.format(urlbase, listID), params={'t': token}, headers=agent)
    return r.json()
