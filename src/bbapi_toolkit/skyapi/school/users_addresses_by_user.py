def get(client: object, user_id: int) -> dict:
    """Get addresses for the given user.

    Documentation:
        https://developer.sky.blackbaud.com/docs/services/school/operations/V1UsersByUser_idAddressesGet

    Args:
        client (object): The SKY API client object.
        user_id (int): The Blackbaud ID for the requested user.

    Returns:
        Dictionary of results.
    """
    url = f'https://api.sky.blackbaud.com/school/v1/users/{user_id}/addresses'
    return client.get(url)
