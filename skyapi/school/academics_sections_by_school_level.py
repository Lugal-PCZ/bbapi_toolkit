def get(client: object, level_num: int, school_year: str = None) -> dict:
    """Get the list of sections for the level and school year indicated.

    Documentation:
        https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsSectionsGet

    Args:
        client (object): The SKY API client object.
        school_year (str): The school year. Defaults to the current year if not specified.

    Returns:
        Dictionary of results.
    """
    url = f'https://api.sky.blackbaud.com/school/v1/academics/sections'
    params = {'level_num': level_num}
    if school_year:
        params['school_year'] = school_year
    return client.get(url, params)
