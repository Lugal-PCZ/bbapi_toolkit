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
    url = f'https://api.sky.blackbaud.com/school/v1/academics/departments'
    params = {}
    if level_id:
        params['level_id'] = level_id
    return client.get(url, params)
