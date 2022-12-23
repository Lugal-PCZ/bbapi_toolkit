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
    url = f'https://api.sky.blackbaud.com/school/v1/legacy/lists/{list_id}'
    return client.get(url)
