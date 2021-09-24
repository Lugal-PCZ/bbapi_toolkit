def get(client: object, schedule_set_id: int) -> dict:
    """Get the detailed rotation for the schedule set indicated.

    Documentation:
        https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsSchedulesSetsBySchedule_set_idGet

    Args:
        client (object): The SKY API client object.
        schedule_set_id (int): The id of the requested schedule set.

    Returns:
        Dictionary of results.
    """
    url = f'https://api.sky.blackbaud.com/school/v1/academics/schedules/sets/{schedule_set_id}'
    return client.get(url)
