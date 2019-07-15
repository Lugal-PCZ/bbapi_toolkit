from ... import requests
from ... import urlbase
from ... import agent
from ... import token


def get_assignments_for_class(leadSectionId: int) -> list:
    """ Return a list of assignments for a course, regardless of section.

    Documentation:
        https://docs.blackbaud.com/on-api-docs/api/academics/assignments/get-assignment

    Args:
        leadSectionId (int): The Lead Section ID of the requested section.

    Returns:
        List of dictionaries.
    """
    r = requests.get('{}/academics/assignment'.format(urlbase), params={'t': token, 'leadSectionId': leadSectionId}, headers=agent)
    return r.json()
