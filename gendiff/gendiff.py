def create_list_key(dict1, dict2):
    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())
    if keys1 == keys2:
        return keys1
    return set(keys1 + keys2)

def to_string(value_to_str, depth):
    if value_to_str is None:
        return 'null'

    if isinstance(value_to_str, bool):
        return str(value_to_str).lower()

    if isinstance(value_to_str, dict):
        result = []
        indent = make_indent(depth + 1)
        for key, value_to_str in value_to_str.items():
            str_value = to_string(value_to_str, depth + 1)
            result.append(
                '{0}    {1}: {2}\n'.format(indent, key, str_value),
            )
        return '{{\n{0}{1}}}'.format(''.join(result), indent)

    return value_to_str

def make_indent(depth, indent_size=4, indent_type=' '):
    return indent_type * indent_size * depth

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
    result = my_print(keys)
    print(result)
    

def my_print(keys, depth = 0):
    indent = make_indent(depth)
    result_str = ''
    for key in keys:
        if key['state'] == 'NESTED':
            result_str += f'{indent}   {key["key"]}: ' + '{\n'
            res = my_print(key['CHILDREN'], depth + 1)
            result_str += res 
            result_str += '{0}{1}\n'.format(indent * 2, '}')
        elif key['state'] == 'updated':
            result_str += f'{indent} - {key["key"]}: {to_string(key["new_value"], depth)}\n'
            result_str += f'{indent} - {key["key"]}: {to_string(key["old_value"], depth)}\n'
        elif key['state'] == 'plus':
            result_str += f'{indent} + {key["key"]}: {to_string(key["value"], depth)}\n'
        elif key['state'] == 'minus':
            result_str += f'{indent} - {key["key"]}: {to_string(key["value"], depth)}\n'
    return result_str
