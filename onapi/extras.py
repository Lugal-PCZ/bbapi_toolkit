# Simple utilities, of general use to the Blackbaud community, that leverage the ON API.
# More complex interactions or data parsing should be done in your own code, not in BBAPI_Toolkit.

import requests
import json

from . import urlbase
from . import token
from . import agent
from .endpoints.constituents import  user


def get_parent_emails_for_student(userId: int) -> list:
    """Get email addresses for the parents of a Blackbaud user.

    Args:
        userId (int): The Blackbaud user ID for the requested user.

    Returns:
        List of the results.
    """
    parentemails = []
    student = user.get_user_extended(userId)
    try:
        for each in student['Relationships']:
            try:
                if each['ParentAccess'] == True:
                    parent = user.get_user(each['Id'])
                    parentemails.append(parent['Email'])
            except:
                pass
    except:
        pass
    return parentemails
