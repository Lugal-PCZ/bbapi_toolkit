import requests as _requests


def get_school_years(client: object) -> list:
    """ Returns information about all school years.

    Documentation:
        https://docs.blackbaud.com/on-api-docs/api/schoolinfo/get-allschoolyears

    Args:
        client (object): The ON API client object.

    Returns:
        List of dictionaries.
    """
    params = {'t': client.token}
    r = _requests.get(
        f'{client.urlbase}/schoolinfo/allschoolyears',
        params=params,
        headers=client.agent,
    )
    return r.json()


def get_school_terms(client: object, schoolyear: str) -> list:
    """ Returns a list of terms for the school year provided.

    Documentation:
        https://docs.blackbaud.com/on-api-docs/api/schoolinfo/get-term

    Args:
        client (object): The ON API client object.
        schoolyear (str): The label of the school year requested, as in "2021 - 2022".

    Returns:
        List of dictionaries.
    """
    params = {'t': client.token}
    if schoolyear:
        params['schoolYear'] = schoolyear
    r = _requests.get(
        f'{client.urlbase}/schoolinfo/term',
        params=params,
        headers=client.agent,
    )
    return r.json()


def get_school_levels(client: object) -> list:
    """ Returns information about school levels.

    Documentation:
        https://docs.blackbaud.com/on-api-docs/api/schoolinfo/get-schoollevel

    Args:
        client (object): The ON API client object.

    Returns:
        List of dictionaries.
    """
    params = {'t': client.token}
    r = _requests.get(
        f'{client.urlbase}/schoolinfo/schoollevel',
        params=params,
        headers=client.agent,
    )
    return r.json()


def get_grade_levels(client: object) -> list:
    """ Returns information about grade levels.

    Documentation:
        https://docs.blackbaud.com/on-api-docs/api/schoolinfo/get-gradelevel

    Args:
        client (object): The ON API client object.

    Returns:
        List of dictionaries.
    """
    params = {'t': client.token}
    r = _requests.get(
        f'{client.urlbase}/schoolinfo/gradelevel',
        params=params,
        headers=client.agent,
    )
    return r.json()
