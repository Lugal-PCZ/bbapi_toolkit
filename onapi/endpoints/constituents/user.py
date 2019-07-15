from ... import requests
from ... import urlbase
from ... import agent
from ... import token

import json
from typing import Union


def get_user(userId: int) -> dict:
    """Get basic information for a Blackbaud user.

    Documentation:
        https://docs.blackbaud.com/on-api-docs/api/constituents/user/get-user-ID

    Args:
        userId (int): The Blackbaud user ID for the requested user.

    Returns:
        Dictionary of the results.
    """
    r = requests.get('{}/user/{}'.format(urlbase, userId), params={'t': token}, headers=agent)
    return r.json()
get_user_basic_info = get_user  ## Function alias with a nicer name than the ON API endpoint.


def get_users(roleIDs: Union[int, list], **kwargs) -> list:
    """Get basic information for a Blackbaud user.

    Documentation:
        https://docs.blackbaud.com/on-api-docs/api/constituents/user/get-user-all

    Args:
        roleIDs (Union[int, list]): The Blackbaud role ids to search.
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
    params = {'t': token, 'roleIDs': roleIDs}
    params.update(kwargs)
    r = requests.get('{}/user/all'.format(urlbase), params=params, headers=agent)
    return r.json()


def get_user_extended(userId: int) -> dict:
    """Get extended information for a Blackbaud user.

    Documentation:
        https://docs.blackbaud.com/on-api-docs/api/constituents/user/get-user-extended-ID

    Args:
        userId (int): The Blackbaud user ID for the requested user.

    Returns:
        Dictionary of the results.
    """
    r = requests.get('{}/user/extended/{}'.format(urlbase, userId), params={'t': token}, headers=agent)
    return r.json()


def get_all_user_extended(userId: int, relationship: bool=False) -> dict:
    """Get extended information for a Blackbaud user, regardless of publish settings.

    Documentation:
        https://docs.blackbaud.com/on-api-docs/api/constituents/user/get-user-extended-all

    Args:
        userId (int): The Blackbaud user ID for the requested user.
        relationship (bool): Enter True if the userId's relationship should be returned.

    Returns:
        Dictionary of the results.
    """
    params = {'t': token}
    if relationship:
        params.update({'relationship': relationship})
    r = requests.get('{}/user/extended/all/{}'.format(urlbase, userId), params=params, headers=agent)
    return r.json()
get_user_extended_info = get_all_user_extended  ## Function alias with a nicer name than the ON API endpoint.


def post_user(FirstName: str, LastName: str) -> int:
    """Creates a new Blackbaud user.

    Documentation:
        https://on-api.developer.blackbaud.com/API/constituents/user/post-user/

    Args:
        firstname (str): The user's first name.
        lastname (str): The user's last name.

    Returns:
        Blackbaud user ID of the newly-created user.
    """
    newuser = {'FirstName': FirstName, 'LastName': LastName}
    headers = {'Content-Type': 'application/json'}
    headers.update(agent)
    r = requests.post("{}/user?t={}".format(urlbase, token), data=json.dumps(newuser), headers=headers)
    return r.json()['Message']
create_user = post_user  ## Function alias with a nicer name than the ON API endpoint.


def put_user(userId: int, fields: dict) -> int:
    """Updates the indicated Blackbaud user with the data provided.

    Documentation:
        https://on-api.developer.blackbaud.com/API/constituents/user/put-user-ID/

    Args:
        userId (int): The Blackbaud user ID for the requested user.
        fields (dict): The data to be updated for the indicated user, in {'field': 'value'} format.
            Consult the online documentation for details about the field names and types.

    Returns:
        Status code of the http request.
    """
    headers = {'Content-Type': 'application/json'}
    headers.update(agent)
    print(headers)
    r = requests.put("{}/user/{}/?t={}".format(urlbase, userId, token), data=json.dumps(fields), headers=headers)
    return r.status_code
update_user = put_user  ## Function alias with a nicer name than the ON API endpoint.


def delete_user(userId: int, prompt: bool = True) -> bool:
    """Deletes the indicated Blackbaud user.

    Documentation:
        https://on-api.developer.blackbaud.com/API/constituents/user/del-user-ID/

    Args:
        userId (int): The Blackbaud user ID for the user to delete.
        prompt (int): Whether or not to prompt to confirm the deletion of the user.
            Default behavior is to prompt for confirmation.

    Returns:
        Boolean of whether or not the user was deleted.
        Note: If prompt is False and the userId doesn't exist, no error is raised.
    """
    deleteuser = not prompt
    if prompt:
        user = get_user(userId)
        if 'Error' in user:
            print(user['Error'])
        else:
            print('\nDelete the following user?')
            print('  | "UserId": {}'.format(user['UserId']))
            print('  | "FirstName": {}'.format(user['FirstName']))
            print('  | "LastName": {}'.format(user['LastName']))
            print('  | "Email": {}'.format(user['Email']))
            print('  | "HostId": {}'.format(user['HostId']))
            print('  | "InsertDate": {}'.format(user['InsertDate']))
            response = input('[yN]: ').upper()
            if response == 'Y':
                deleteuser = True
            else:
                print('User {} will not be deleted.'.format(user['UserId']))
    if deleteuser:
        headers = {'Content-Type': 'application/json'}
        headers.update(agent)
        requests.delete("{}/user/{}".format(urlbase, userId), params={'t': token}, headers=headers)
    return deleteuser
