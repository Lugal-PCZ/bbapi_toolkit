def get(client: object, level_num: int, school_year: str = None, group_type: int = None) -> dict:
    """Get the list of schedule sets for the level, school year, and group type indicated.

    Documentation:
        https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsSchedulesSetsGet

    Args:
        client (object): The SKY API client object.
        school_year (str): The school year. Defaults to the current year if not specified.
        group_type (int): The group type. Defaults to academic (1) if not specified.

    Returns:
        Dictionary of results.
    """
    url = f'https://api.sky.blackbaud.com/school/v1/academics/schedules/sets'
    params = {'level_num': level_num}
    if school_year:
        params['school_year'] = school_year
    if group_type:
        params['group_type'] = group_type
    return client.get(url, params)
