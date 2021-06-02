def create_list_key(dict1, dict2):
    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())
    if keys1 == keys2:
        return keys1
    return set(keys1 + keys2)


def generate_diff(data1, data2):
    keys = create_list_key(data1, data2)
    for key in sorted(keys):
        if key in data1 and key in data2:
            if data1.get(key) == data2.get(key):
                print(f'  {key}: {data1.get(key)}')
            else:
                print(f'- {key}: {data1.get(key)}')
                print(f'+ {key}: {data2.get(key)}')
        if key in data1 and key not in data2:
            print(f'- {key}: {data1.get(key)}')
        if key in data2 and key not in data1:
            print(f'+ {key}: {data2.get(key)}')
