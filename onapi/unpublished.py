# Note these are UNPUBLISHED endpoints. Though they may be useful, they cannot be relied
# upon for production purposes, and Blackbaud may change or restrict them without warning.

import requests as _requests


def get_rooms(client: object) -> list:
    """Get buildings and rooms.

    Args:
        client (object): The ON API client object.

    Returns:
        List of dictionaries.
    """
    r = _requests.get(
        f'{client.urlbase}/venue/buildinglist',
        params={'t': client.token},
        headers=client.agent,
    )
    return r.json()
