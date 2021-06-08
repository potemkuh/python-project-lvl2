import json


dict1 = json.load(open('gendiff/files/file3.json','r'))
dict2 = json.load(open('gendiff/files/file4.json','r'))


def create_list_key(dict1, dict2):
    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())
    if keys1 == keys2:
        return keys1
    return set(keys1 + keys2)


def generate_diff(data1, data2):
    keys = create_list_key(data1, data2)
    result_str = '{\n'
    for key in sorted(keys):
        if isinstance(data1.get(key), bool):
            data1[key] = str(data1.get(key)).lower()
        if isinstance(data2.get(key), bool):
            data2[key] = str(data2.get(key)).lower()
        if key in data1 and key in data2:
            if data1.get(key) == data2.get(key):
                result_str += f'    {key}: {data1.get(key)}\n'
            else:
                result_str += f'  - {key}: {data1.get(key)}\n'
                result_str += f'  + {key}: {data2.get(key)}\n'
        if key in data1 and key not in data2:
            result_str += f'  - {key}: {data1.get(key)}\n'
        if key not in data1 and key in data2:
            result_str += f'  + {key}: {data2.get(key)}\n'
    return result_str + '}'

print(create_list_key(dict1, dict2))