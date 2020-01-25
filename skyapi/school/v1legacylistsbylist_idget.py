def get(client: object, list_id: int) -> list:
    """Get data from a pre-built Blackbaud list.

    Documentation:
        https://developer.sky.blackbaud.com/docs/services/school/operations/V1LegacyListsByList_idGet

    Args:
        client (object): The SKY API client object.
        list_id (int): The Blackbaud ID for the requested list.

    Returns:
        List of dictionaries.
    """
    client.rate_limiter()
    result_set = []
    r = client.session.get(
        f'https://api.sky.blackbaud.com/school/v1/legacy/lists/{list_id}',
        headers=client.headers,
    )
    for each_row in r.json()['rows']:
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
