import requests as _requests


def get_list(client: object, listID: int) -> list:
    """Get data from a pre-built Blackbaud list.

    Documentation:
        https://docs.blackbaud.com/on-api-docs/api/list/get-list-id

    Args:
        client (object): The ON API client object.
        listID (int): The Blackbaud ID for the requested list.

    Returns:
        List of dictionaries.
    """
    r = _requests.get(
        f'{client.urlbase}/list/{listID}',
        params={'t': client.token},
        headers=client.agent,
    )
    return r.json()
