def get(client: object, list_id: int) -> dict:
    """Get data from a pre-built Blackbaud list.

    Documentation:
        https://developer.sky.blackbaud.com/docs/services/school/operations/V1LegacyListsByList_idGet

    Args:
        client (object): The SKY API client object.
        list_id (int): The Blackbaud ID for the requested list.

    Returns:
        Dictionary of results.
    """
    client.rate_limiter()
    r = client.session.get(
        f'https://api.sky.blackbaud.com/school/v1/legacy/lists/{list_id}',
        headers=client.headers,
    )
    return r.json()
