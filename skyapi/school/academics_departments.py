def get(client: object, level_id: int = None) -> dict:
    """Returns the academic departments for the school level indicated.

    Documentation:
        https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsDepartmentsGet

    Args:
        client (object): The SKY API client object.
        level_id (int): The id of the requested school level.

    Returns:
        Dictionary of results.
    """
    client.rate_limiter()
    params = {}
    if level_id:
        params['level_id'] = level_id
    r = client.session.get(
        f'https://api.sky.blackbaud.com/school/v1/academics/departments',
        params=params,
        headers=client.headers,
    )
    return r.json()
