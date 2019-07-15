from ... import requests
from ... import urlbase
from ... import agent
from ... import token


def get_roles() -> list:
    """Get information about the roles in Blackbaud.

    Documentation:
        https://docs.blackbaud.com/on-api-docs/api/constituents/role/get-listall

    Returns:
        List of dictionaries.
    """
    r = requests.get('{}/role/ListAll'.format(urlbase), params={'t': token}, headers=agent)
    return r.json()
