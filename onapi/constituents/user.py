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
    url = f'/user/{userId}'
    return client.get(url)
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
    url = '/user/all'
    if isinstance(roleIDs, list):
        roleIDs = ','.join(map(str, roleIDs))
    params = {'roleIDs': roleIDs}
    params.update(kwargs)
    return client.get(url, params)


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
    url = f'/user/extended/{userId}'
    return client.get(url)


def get_all_user_extended(client: object, userId: int, relationship: bool = False) -> dict:
    """Get extended information for a Blackbaud user, regardless of their profile publish settings.

    Documentation:
        https://docs.blackbaud.com/on-api-docs/api/constituents/user/get-user-extended-all

    Args:
        client (object): The ON API client object.
        userId (int): The Blackbaud user ID for the requested user.
        relationship (bool): Enter True if the userId's relationship should be returned.
            Note: It appears that this value is ignored, and relationship is always returned.

    Returns:
        Dictionary of the results.
    """
    url = f'/user/extended/all/{userId}'
    params = {}
    if relationship:
        params['relationship'] = relationship
    return client.get(url, params)
get_user_extended_info = get_all_user_extended  ## Function alias with a nicer name than the ON API endpoint.


def post_user(client: object, FirstName: str, LastName: str) -> int:
    """Creates a new Blackbaud user.

    Documentation:
        https://docs.blackbaud.com/on-api-docs/api/constituents/user/post-user/

    Args:
        client (object): The ON API client object.
        firstname (str): The user's first name.
        lastname (str): The user's last name.

    Returns:
        Blackbaud user ID of the newly-created user.
    """
    url = '/user'
    params = {'FirstName': FirstName, 'LastName': LastName}
    return client.post(url, params)['Message']
create_user = post_user  ## Function alias with a nicer name than the ON API endpoint.


def put_user(client: object, userId: int, fields: dict) -> int:
    """Updates the indicated Blackbaud user with the data provided.

    Documentation:
        https://docs.blackbaud.com/on-api-docs/api/constituents/user/put-user-ID/

    Args:
        client (object): The ON API client object.
        userId (int): The Blackbaud user ID for the requested user.
        fields (dict): The data to be updated for the indicated user, in {'field': 'value'} format.
            Consult the online documentation for details about the field names and types.

    Returns:
        Status code of the http request.
    """
    url = f'/user/{userId}'
    return client.put(url, fields)
update_user = put_user  ## Function alias with a nicer name than the ON API endpoint.


def delete_user(client: object, userId: int, prompt: bool = True) -> bool:
    """Deletes the indicated Blackbaud user.

    Documentation:
        https://docs.blackbaud.com/on-api-docs/api/constituents/user/del-user-ID/

    Args:
        client (object): The ON API client object.
        userId (int): The Blackbaud user ID for the user to delete.
        prompt (int): Whether or not to prompt to confirm the deletion of the user.
            Default behavior is to prompt for confirmation.

    Returns:
        Boolean of whether or not the user was deleted.
        Note: If prompt is False and the userId doesn't exist, no error is raised.
    """
    url = f'/user/{userId}'
    deleteuser = not prompt
    if prompt:
        user = get_user(client, userId)
        if 'Error' in user:
            message = user['Error']
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
                message = f'User {userId} '
                if int(client.delete(url)['Message']) == userId:
                    message += 'was deleted.'
                else:
                    message += 'was not deleted.'
            else:
                message = f'User {userId} will not be deleted.'
    return message
