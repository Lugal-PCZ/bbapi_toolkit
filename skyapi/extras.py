def get_cleaned_legacy_list(client: object, list_id: int) -> list:
    """Get data from a pre-built Blackbaud list, cleaned and returned as a list.

    Args:
        client (object): The SKY API client object.
        list_id (int): The Blackbaud ID for the requested list.

    Returns:
        List of dictionaries.
    """
    from . import school
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
