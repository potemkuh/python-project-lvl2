from gendiff.formatters import render_stylish, render_plain, render_json
from gendiff.constans import (
    ADDED,
    CHILDREN,
    KEY,
    NESTED,
    REMOVED,
    TYPE,
    UNCHANGED,
    VALUE,
    TYPE,
    UPDATED,
    ORIGIN,
)


def create_list_key(dict1, dict2):
    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())
    if keys1 == keys2:
        return keys1

    return set(keys1 + keys2)


def create_build(data1, data2):
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
                    CHILDREN: create_build(data1[key], data2[key]),
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


def choice_of_style(diff, format_name):
    if format_name == 'stylish':
        res = render_stylish.render_stylish(diff)
    elif format_name == 'plain':
        res = render_plain.render_plain(diff)
    elif format_name == 'json':
        res = render_json.render_json(diff)
    return res

def build_diff(data1, data2, format_name='stylish'):
    diff = {
        TYPE: ORIGIN,
        CHILDREN: create_build(data1, data2),
    }
    return choice_of_style(diff, format_name)
