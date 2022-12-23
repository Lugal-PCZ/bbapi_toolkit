def get_roles(client: object) -> list:
    """Get information about the roles in Blackbaud.

    Documentation:
        https://docs.blackbaud.com/on-api-docs/api/constituents/role/get-listall

    Args:
        client (object): The ON API client object.

    Returns:
        List of dictionaries.
    """
    url = '/role/ListAll'
    return client.get(url)
