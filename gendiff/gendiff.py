ADDED = 'added'
CHILDREN = 'children'
KEY = 'key'
NESTED = 'nested'
ORIGIN = 'origin'
REMOVED = 'removed'
TYPE = 'type'
UNCHANGED = 'unchanged'
UPDATED = 'updated'
VALUE = 'value'


def create_list_key(dict1, dict2):
    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())
    if keys1 == keys2:
        return keys1

    return set(keys1 + keys2)

def render_stylish(diff, depth=0):
    diff_type = diff[TYPE]
    key = diff.get(KEY)
    indent = make_indent(depth)
    children = diff.get(CHILDREN)

    if diff_type == ORIGIN:
        rows = ['{0}{1}\n'.format(
            indent,
            render_stylish(child, depth),
        ) for child in children]
        return '{{\n{0}}}'.format(''.join(rows))

    if diff_type == NESTED:
        rows = ['{0}\n'.format(
            render_stylish(child, depth + 1),
        ) for child in children]
        return '{0}    {1}: {{\n{2}{3}}}'.format(
            indent,
            key,
            ''.join(rows),
            make_indent(depth + 1),
        )

    if diff_type == ADDED:
        return '{0}  + {1}: {2}'.format(
            indent,
            key,
            to_string(diff['value'], depth),
        )

    if diff_type == REMOVED:
        return '{0}  - {1}: {2}'.format(
            indent,
            key,
            to_string(diff['value'], depth),
        )

    if diff_type == UPDATED:
        str1 = '{0}  - {1}: {2}'.format(
            indent,
            key,
            to_string(diff['old_value'], depth),
        )
        str2 = '{0}  + {1}: {2}'.format(
            indent,
            key,
            to_string(diff['new_value'], depth),
        )
        return '\n'.join([str1, str2])

    if diff_type == UNCHANGED:
        return '{0}    {1}: {2}'.format(
            indent,
            key,
            to_string(diff['value'], depth),
        )

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

def calculate_diff(data1, data2):
    keys = create_list_key(data1, data2)
    result_diff = list()
    for key in sorted(keys):
        if key not in data1:
            result_diff.append({
                TYPE: ADDED,
                KEY: key,
                VALUE: data2[key],
            })
            continue

        if key not in data2:
            result_diff.append({
                TYPE: REMOVED,
                KEY: key,
                VALUE: data1[key],
            })
            continue

        if isinstance(data1[key], dict):
            if isinstance(data2[key], dict):
                result_diff.append({
                    TYPE: NESTED,
                    KEY: key,
                    CHILDREN: calculate_diff(data1[key], data2[key]),
                })
                continue

        if data1[key] != data2[key]:
            result_diff.append({
                TYPE: UPDATED,
                KEY: key,
                'old_value': data1[key],
                'new_value': data2[key],
            })
            continue

        result_diff.append({
            TYPE: UNCHANGED,
            KEY: key,
            VALUE: data1[key],
        })

    return result_diff

def generate_diff(data1, data2):
    diff = {
        TYPE: ORIGIN,
        CHILDREN: calculate_diff(data1, data2),
    }
    res = render_stylish(diff)
    print(res)
    