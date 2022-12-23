def get(client: object) -> dict:
    """Get a list of buildings and rooms.

    Documentation:
        https://developer.sky.blackbaud.com/docs/services/school/operations/V1VenuesBuildingsGet

    Args:
        client (object): The SKY API client object.

    Returns:
        Dictionary of results.
    """
    url = f'https://api.sky.blackbaud.com/school/v1/venues/buildings'
    return client.get(url)
