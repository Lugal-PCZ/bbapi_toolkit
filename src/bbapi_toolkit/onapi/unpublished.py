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
    url = '/venue/buildinglist'
    return client.get(url)
