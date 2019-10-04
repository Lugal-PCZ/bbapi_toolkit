import requests as _requests
import json as _json
from typing import Union as _Union


def get_user(client: object, userId: int) -> dict:
    """Get basic information for a Blackbaud user.

    Documentation:
        https://docs.blackbaud.com/on-api-docs/api/constituents/user/get-user-ID

    Args:
        client (object): The ON API client object.
        userId (int): The Blackbaud user ID for the requested user.

    Returns:
        Dictionary of the results.
    """
    r = _requests.get(
        f'{client.urlbase}/user/{userId}',
        params={'t': client.token},
        headers=client.agent,
    )
    return r.json()
get_user_basic_info = get_user  ## Function alias with a nicer name than the ON API endpoint.


def get_users(client: object, roleIDs: _Union[int, list], **kwargs) -> list:
    """Get basic information for a Blackbaud user.

    Documentation:
        https://docs.blackbaud.com/on-api-docs/api/constituents/user/get-user-all

    Args:
        client (object): The ON API client object.
        roleIDs (_Union[int, list]): The Blackbaud role ids to search.
        **kwargs: Optional filters limiting the results. The options are:
            firstname (str): Performs a partial match on user first names.
            lastname (str): Performs a partial match on user last names.
            email (str): Performs a partial match on user emails.
            maidenname (str): Performs a partial match on maiden names.
            gradyear (str): 4 digit year and limits search to users of this grad year.
            endgradyear (int): When populated in conjuction with gradyear, search becomes limited to all grad years between gradyear and endgradyear, inclusive.
            startrow (int): Defaults to 1.
            endrow (int): Defaults to 200. Endrow has to be greater than startrow. We limit the return to 200 rows

    Returns:
        List of dictionaries.
    """
    if type(roleIDs) == list:
        roleIDs = ','.join(map(str, roleIDs))
    params = {'t': client.token, 'roleIDs': roleIDs}
    params.update(kwargs)
    r = _requests.get(
        f'{client.urlbase}/user/all',
        params=params,
        headers=client.agent,
    )
    return r.json()


def get_user_extended(client: object, userId: int) -> dict:
    """Get extended information for a Blackbaud user.

    Documentation:
        https://docs.blackbaud.com/on-api-docs/api/constituents/user/get-user-extended-ID

    Args:
        client (object): The ON API client object.
        userId (int): The Blackbaud user ID for the requested user.

    Returns:
        Dictionary of the results.
    """
    r = _requests.get(
        f'{client.urlbase}/user/extended/{userId}',
        params={'t': client.token},
        headers=client.agent,
    )
    return r.json()


def get_all_user_extended(client: object, userId: int, relationship: bool=False) -> dict:
    """Get extended information for a Blackbaud user, regardless of publish settings.

    Documentation:
        https://docs.blackbaud.com/on-api-docs/api/constituents/user/get-user-extended-all

    Args:
        client (object): The ON API client object.
        userId (int): The Blackbaud user ID for the requested user.
        relationship (bool): Enter True if the userId's relationship should be returned.

    Returns:
        Dictionary of the results.
    """
    params = {'t': client.token}
    if relationship:
        params.update({'relationship': relationship})
    r = _requests.get(
        f'{client.urlbase}/user/extended/all/{userId}',
        params=params,
        headers=client.agent,
    )
    return r.json()
get_user_extended_info = get_all_user_extended  ## Function alias with a nicer name than the ON API endpoint.


def post_user(client: object, FirstName: str, LastName: str) -> int:
    """Creates a new Blackbaud user.

    Documentation:
        https://on-api.developer.blackbaud.com/API/constituents/user/post-user/

    Args:
        client (object): The ON API client object.
        firstname (str): The user's first name.
        lastname (str): The user's last name.

    Returns:
        Blackbaud user ID of the newly-created user.
    """
    newuser = {'FirstName': FirstName, 'LastName': LastName}
    headers = {'Content-Type': 'application/json'}
    headers.update(client.agent)
    r = _requests.post(
        f'{client.urlbase}/user?t={client.token}',
        data=_json.dumps(newuser),
        headers=headers,
    )
    return r.json()['Message']
create_user = post_user  ## Function alias with a nicer name than the ON API endpoint.


def put_user(client: object, userId: int, fields: dict) -> int:
    """Updates the indicated Blackbaud user with the data provided.

    Documentation:
        https://on-api.developer.blackbaud.com/API/constituents/user/put-user-ID/

    Args:
        client (object): The ON API client object.
        userId (int): The Blackbaud user ID for the requested user.
        fields (dict): The data to be updated for the indicated user, in {'field': 'value'} format.
            Consult the online documentation for details about the field names and types.

    Returns:
        Status code of the http request.
    """
    headers = {'Content-Type': 'application/json'}
    headers.update(client.agent)
    print(headers)
    r = _requests.put(
        f'{client.urlbase}/user/{userId}/?t={client.token}',
        data=_json.dumps(fields),
        headers=headers,
    )
    return r.status_code
update_user = put_user  ## Function alias with a nicer name than the ON API endpoint.


def delete_user(client: object, userId: int, prompt: bool = True) -> bool:
    """Deletes the indicated Blackbaud user.

    Documentation:
        https://on-api.developer.blackbaud.com/API/constituents/user/del-user-ID/

    Args:
        client (object): The ON API client object.
        userId (int): The Blackbaud user ID for the user to delete.
        prompt (int): Whether or not to prompt to confirm the deletion of the user.
            Default behavior is to prompt for confirmation.

    Returns:
        Boolean of whether or not the user was deleted.
        Note: If prompt is False and the userId doesn't exist, no error is raised.
    """
    deleteuser = not prompt
    if prompt:
        user = get_user(client, userId)
        if 'Error' in user:
            print(user['Error'])
        else:
            print('\nDelete the following user?')
            print(f'  | "UserId": {user["UserId"]}')
            print(f'  | "FirstName": {user["FirstName"]}')
            print(f'  | "LastName": {user["LastName"]}')
            print(f'  | "Email": {user["Email"]}')
            print(f'  | "HostId": {user["HostId"]}')
            print(f'  | "InsertDate": {user["InsertDate"]}')
            response = input('[yN]: ').upper()
            if response == 'Y':
                deleteuser = True
            else:
                print(f'User {user["UserId"]} will not be deleted.')
    if deleteuser:
        headers = {'Content-Type': 'application/json'}
        headers.update(client.agent)
        _requests.delete(
            f'{client.urlbase}/user/{userId}',
            params={'t': client.token},
            headers=headers,
        )
    return deleteuser
