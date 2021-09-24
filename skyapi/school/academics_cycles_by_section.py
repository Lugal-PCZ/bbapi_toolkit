def get(client: object, section_id: int, duration_id: int = None, group_type: int = None) -> dict:
    """Get the list of cycles for the section indicated.

    Documentation:
        https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsSectionsBySection_idCyclesGet

    Args:
        client (object): The SKY API client object.
        section_id (int): The id of the section.
        duration_id (int): The ID of the term for which you want to return cycles. Defaults to the current term for the section provided.
        group_type (int): The Group Type for the section specified. Defaults to academics (1).

    Returns:
        Dictionary of results.
    """
    url = f'https://api.sky.blackbaud.com/school/v1/academics/sections/{section_id}/cycles'
    params = {}
    if duration_id:
        params['duration_id'] = duration_id
    if group_type:
        params['group_type'] = group_type
    return client.get(url, params)
