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
        if key not in dict2:
            result.append({
                'key': key,
                'state': 'minus',
                'value': dict1[key]
            })
            continue
        elif key not in dict1:
            result.append({
                'key': key,
                'state': 'plus',
                'value': dict2[key]
            })
            continue
        elif isinstance(dict1[key], dict):
            if isinstance(dict2[key], dict):
                result.append({
                    'key': key,
                    'state': 'NESTED',                    
                    'CHILDREN': calculate_diff(dict1[key], dict2[key]),
                })
                continue
        
        result.append({
            'key': key,
            'state': 'updated',
            'old_value': dict1[key],
            'new_value': dict2[key],
            })
            
    return result


def generate_diff(data1, data2):
    keys = calculate_diff(data1, data2)
    print(keys)
    #result = my_print(keys)
    #print(result)
    

def my_print(keys, space = '    '):
    result_str = ''
    for key in keys:
        if key['state'] == 'NESTED':
            result_str += f'{space}   {key["key"]}: ' + '{\n'
            res = my_print(key['CHILDREN'], space  + space)
            result_str += res
        elif key['state'] == 'updated':
            result_str += f'{space} - {key["key"]}: {key["new_value"]}\n'
            result_str += f'{space} - {key["key"]}: {key["old_value"]}\n'
        elif key['state'] == 'plus':
            result_str += f'{space} + {key["key"]}: {key["value"]}\n'
        elif key['state'] == 'minus':
            result_str += f'{space} - {key["key"]}: {key["value"]}\n'
    return result_str
