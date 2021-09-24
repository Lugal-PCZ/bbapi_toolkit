def get(client: object) -> dict:
    """Get a list of core school user roles.

    Documentation:
        https://developer.sky.blackbaud.com/docs/services/school/operations/v1rolesget

    Args:
        client (object): The SKY API client object.

    Returns:
        Dictionary of results.
    """
    url = f'https://api.sky.blackbaud.com/school/v1/roles'
    return client.get(url)
