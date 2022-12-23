# Simple utilities, of general use to the Blackbaud community, that leverage the ON API.
# More complex interactions or data parsing should be done in your own code, not in BBAPI_Toolkit.

from .constituents import user as _user


def get_parent_emails_for_student(client: object, userId: int) -> list:
    """Get email addresses for the parents of a Blackbaud user.

    Args:
        client (object): The ON API client object.
        userId (int): The Blackbaud user ID for the requested user.

    Returns:
        List of the results.
    """
    parentemails = []
    student = _user.get_user_extended(client, userId)
    try:
        for each in student['Relationships']:
            try:
                if each['ParentAccess'] == True:
                    parent = _user.get_user(client, each['Id'])
                    parentemails.append(parent['Email'])
            except:
                pass
    except:
        pass
    return parentemails
