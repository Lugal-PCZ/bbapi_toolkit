def get_assignments_for_class(client: object, leadSectionId: int) -> list:
    """ Return a list of assignments for a course, regardless of section.

    Documentation:
        https://docs.blackbaud.com/on-api-docs/api/academics/assignments/get-assignment

    Args:
        client (object): The ON API client object.
        leadSectionId (int): The Lead Section ID of the requested section.

    Returns:
        List of dictionaries.
    """
    url = '/academics/assignment'
    params = {'leadSectionId': leadSectionId}
    return client.get(url, params)
