def get(client: object, school_year: str = None, offering_type: int = None) -> dict:
    """Get the list of terms for the school year and offering type indicated.

    Documentation:
        https://developer.sky.blackbaud.com/docs/services/school/operations/v1termsget

    Args:
        client (object): The SKY API client object.
        school_year (str): The school year. Defaults to the current year if not specified.
        offering_type (int): The id of the offering type.

    Returns:
        Dictionary of results.
    """
    url = f'https://api.sky.blackbaud.com/school/v1/terms'
    params = {}
    if school_year:
        params['school_year'] = school_year
    if offering_type:
        params['offering_type'] = offering_type
    return client.get(url, params)
