def get(client: object) -> dict:
    """Get a list of school levels.

    Documentation:
        https://developer.sky.blackbaud.com/docs/services/school/operations/v1levelsget

    Args:
        client (object): The SKY API client object.

    Returns:
        Dictionary of results.
    """
    url = f'https://api.sky.blackbaud.com/school/v1/levels'
    return client.get(url)
