def get(client: object, level_num: int, start_date: str, end_date: str, offering_type: int = None) -> dict:
    """Get the master schedule days within the date range indicated.

    Documentation:
        https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsSchedulesMasterGet

    Args:
        client (object): The SKY API client object.
        level_num (int): The id of the school level.
        start_date (str): Start of the date range (inclusive), in the format 'yyyy-mm-dd'.
        end_date (str): End of the date range (inclusive), in the format 'yyyy-mm-dd'.
        offering_type (int): Id of the group type. Defaults to all offering types if not specified.

    Returns:
        Dictionary of results.
    """
    url = f'https://api.sky.blackbaud.com/school/v1/academics/schedules/master?level_num={level_num}&start_date={start_date}&end_date={end_date}'
    params = {}
    if offering_type:
        params['offering_type'] = offering_type
    return client.get(url, params)
