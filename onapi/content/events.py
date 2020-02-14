import requests as _requests


def get_event_categories(client: object) -> list:
    """ Returns information about all the event categories.

    Documentation:
        http://on-api.developer.blackbaud.com/API/content/events/get-event-cat-all/

    Args:
        client (object): The ON API client object.

    Returns:
        List of dictionaries.
    """
    r = _requests.get(
        f'{client.urlbase}/event/category/all',
        params={'t': client.token},
        headers=client.agent,
    )
    return r.json()


def get_events(client: object, categoryID: list) -> list:
    """ Returns information about all the events with the given category ID(s).

    Documentation:
        https://docs.blackbaud.com/on-api-docs/api/content/events/get-event-all

    Args:
        client (object): The ON API client object.
        categoryID (list): The IDs of the categories to return.

    Returns:
        List of dictionaries.
    """
    categories = f'0_{",0_".join(map(str, categoryID))}'
    r = _requests.get(
        f'{client.urlbase}/event/all',
        params={'t': client.token, 'categoryID': categories},
        headers=client.agent,
    )
    return r.json()


def get_event(client: object, id: int) -> list:
    """ Returns information about the requested event.

    Documentation:
        https://docs.blackbaud.com/on-api-docs/api/content/events/get-event

    Args:
        client (object): The ON API client object.
        id (int): The ID of the requested event.

    Returns:
        List of dictionaries.
    """
    r = _requests.get(
        f'{client.urlbase}/event/{id}',
        params={'t': client.token},
        headers=client.agent,
    )
    return r.json()
