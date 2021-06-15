def create_list_key(dict1, dict2):
    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())
    if keys1 == keys2:
        return keys1
    return set(keys1 + keys2)


def calculate_diff(dict1, dict2):
    keys = create_list_key(dict1, dict2)
    result = list()
    print(keys)
    for key in sorted(keys):
        if key not in dict2:
            result.append({
                'key': key,
                'state': 'minus',
                'value': dict1.get(key)
            })
        elif key not in dict1:
            result.append({
                'key': key,
                'state': 'plus',
                'value': dict2.get(key)
            })
        elif isinstance(dict1[key], dict):
            if isinstance(dict2[key], dict):
                result.append({
                    'key': key,
                    'state': 'NESTED',                    
                    'CHILDREN': calculate_diff(dict1[key], dict2[key]),
                })
                continue
        elif key in dict1 and key in dict2:
            if dict1.get(key) != dict2.get(key):
                result.append({
                'key': key,
                'state': 'minus',
                'value': dict1[key]
                })
                result.append({
                'key': key,
                'state': 'plus',
                'value': dict2[key]
                })
            else:
                result.append({
                'key': key,
                'state': 'pass',
                'value': dict1[key]
            })
        elif isinstance(dict1, dict):
            if isinstance(dict2, dict):
                calculate_diff(dict1[key], dict2[key])
        elif key not in dict2:
            result.append({
        'key': key,
        'state': 'minus',
        'value': dict1.get(key)
    })
        elif key not in dict1:
            result.append({
        'key': key,
        'state': 'plus',
        'value': dict2.get(key)
    })
        elif isinstance(dict1[key], dict):
            if isinstance(dict2[key], dict):
                result.append({
            'key': key,
            'state': 'NESTED',
            'value': calculate_diff(dict1[key], dict2[key])
        })
        elif dict1[key] != dict2[key]:
            result.append({
        'key': key,
        'state': 'updated',
        'old_value': dict1[key],
        'new_value': dict2[key],
    })
        else:
            result.append({
    'key': key,
    'state': 'pass',
    'value': dict1[key]
})
    return result


def generate_diff(data1, data2):
    keys = calculate_diff(data1, data2)
    #print(keys)
    my_print(keys, data1, data2)
    



def my_print(keys, data1, data2):    
    new_value = data2.get('new_value')
    old_value = data1.get('old_value')
    result_str = '{\n'
    for key in keys:
        if key['state'] == 'plus':
            result_str += f' + {key}: {data2.get(key)}\n'
        elif key['state'] == 'minus':
            result_str += f' - {key}: {data1.get(key)}\n'
        elif key['state'] == 'pass':
            result_str += f'   {key}: {data1.get(key)}\n'
        elif key['state'] == 'NESTED':
            #my_print(keys, data1.get(key), data2.get(key))
            #print(data1,key)
            print('DATA 1', data1)
            print('KEY', key)
        elif key['updated']:
            result_str += f' + {key}: {data2.get(new_value)}\n'
            result_str += f' - {key}: {data1.get(old_value)}\n'
    return result_str + '}'
    