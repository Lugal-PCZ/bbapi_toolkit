import requests as _requests


def get_roles(client: object) -> list:
    """Get information about the roles in Blackbaud.

    Documentation:
        https://docs.blackbaud.com/on-api-docs/api/constituents/role/get-listall

    Args:
        client (object): The ON API client object.

    Returns:
        List of dictionaries.
    """
    r = _requests.get(
        f'{client.urlbase}/role/ListAll',
        params={'t': client.token},
        headers=client.agent,
    )
    return r.json()
