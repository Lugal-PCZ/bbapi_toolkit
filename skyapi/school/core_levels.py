def get(client: object) -> dict:
    """Get a list of school levels.

    Documentation:
        https://developer.sky.blackbaud.com/docs/services/school/operations/v1levelsget

    Args:
        client (object): The SKY API client object.

    Returns:
        Dictionary of results.
    """
    client.rate_limiter()
    r = client.session.get(
        f'https://api.sky.blackbaud.com/school/v1/levels',
        headers=client.headers,
    )
    return r.json()
