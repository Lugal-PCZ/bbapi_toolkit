from . import school


def get_cleaned_legacy_list(client: object, list_id: int) -> list:
    """Get data from a pre-built Blackbaud list, cleaned and returned as a list.

    Args:
        client (object): The SKY API client object.
        list_id (int): The Blackbaud ID for the requested list.

    Returns:
        List of dictionaries.
    """
    result_set = []
    raw = school.v1legacylistsbylist_idget.get(client, list_id)
    for each_row in raw['rows']:
        new_row = {}
        for each_column in each_row['columns']:
            val = None
            if 'value' in each_column:
                val = each_column['value'].strip()
                if val == 'True':
                    val = True
                elif val == 'False':
                    val = False
            new_pair = {each_column['name']: val}
            new_row = {**new_row, **new_pair}
        result_set.append(new_row)
    return result_set


def get_current_school_year(client: object) -> str:
    """Get the label of the current school year.

    Args:
        client (object): The SKY API client object.

    Returns:
        String label for the current school year.
    """
    years = school.year_list.get(client)
    for each_year in years['value']:
        if each_year['current_year'] == True:
            current_year = each_year['school_year_label']
            break
    return current_year
