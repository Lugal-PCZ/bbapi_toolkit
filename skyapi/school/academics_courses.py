def get(client: object, department_id: int = None, level_id: int = None) -> dict:
    """Returns the academic courses for the indicated department and/or level.

    Documentation:
        https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsCoursesGet

    Args:
        client (object): The SKY API client object.
        department_id (int): The id of the requested department.
        level_id (int): The id of the requested school level.

    Returns:
        Dictionary of results.
    """
    client.rate_limiter()
    params = {}
    if department_id:
        params['department_id'] = department_id
    if level_id:
        params['level_id'] = level_id
    r = client.session.get(
        f'https://api.sky.blackbaud.com/school/v1/academics/courses',
        params=params,
        headers=client.headers,
    )
    return r.json()
