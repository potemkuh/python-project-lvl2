def create_list_key(dict1, dict2):
    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())
    if keys1 == keys2:
        return keys1
    return set(keys1 + keys2)


def calculate_diff(dict1, dict2):
    keys = create_list_key(dict1, dict2)
    result = list()
    for key in sorted(keys):
        if key not in dict1:
            result.append({
                        'key': key,
                        'type': 'added',
                        'value': dict2.get(key)
                            })
        if key not in dict2:
            result.append({
                        'key': key,
                        'type': 'remove',
                        'value': dict1.get(key)
                            })
        if key in dict1 and key in dict2:
            result.append({
                        'key': key,
                        'type': 'added',
                        'value': dict2.get(key)
            })
            result.append({
                        'key': key,
                        'type': 'remove',
                        'value': dict1.get(key)
            })
        if isinstance(dict1.get(key), dict):
            if isinstance(dict2.get(key), dict):
                result.append({
                        'key': key,
                        'type': 'pass',
                        'child': calculate_diff(dict1[key], dict2[key])
                })
    return result


def generate_diff(data1, data2):
    keys = calculate_diff(data1, data2)
    my_print(keys, data1, data2)



def my_print(keys, data1, data2):
    result_str = '{\n'
    for key in keys:
        if key['type'] == 'added':
            result_str += f' + {key}: {data2.get(key)}\n'
        if key['type'] == 'remove':
            result_str += f' - {key}: {data1.get(key)}\n'
        if key['type'] == 'pass':
            generate_diff(data1.get(key), data2.get(key))
            result_str += ' '
            if key['type'] == 'added':
                result_str += f' + {key}: {data2.get(key)}\n'
            if key['type'] == 'remove':
                result_str += f' - {key}: {data1.get(key)}\n'
    return result_str + '}'
