from datetime import date, datetime


def post(client: object, id: int, user_ids: list, section_ids: list, enrollment_date: str = None) -> dict:
    """Enrolls a list of students and/or teachers into a list of sections.

    Documentation:
        https://developer.sky.blackbaud.com/docs/services/school/operations/V1AcademicsSectionsStudentsPost

    Args:
        client (object): The SKY API client object.
        id (int): The duration id of the of the appropriate term, as revealed in the section list (see academics_sections_by_school_level.py).
        user_ids (list): A list of the ids of the students and/or teachers to enroll.
        section_ids (list): A list of the ids of the sections to enroll the students and/or teachers in.
        enrollment_date (str): The enrollment date in ISA-8601 format. Defaults to today's date if omitted.

    Returns:
        Dictionary of results.
    """
    url = f'https://api.sky.blackbaud.com/school/v1/academics/sections/students'
    params = {
        'id': id,
        'user_ids': ','.join([str(x) for x in user_ids]),
        'section_ids': ','.join([str(x) for x in section_ids]),
    }
    if enrollment_date:
        thedate = datetime.fromisoformat(enrollment_date)
        params['enrollment_date'] = datetime(thedate.year, thedate.month, thedate.day, 0, 0).isoformat()
    else:
        now = datetime.now()
        params['enrollment_date'] = datetime(now.year, now.month, now.day).isoformat()
    return client.post(url, params)
