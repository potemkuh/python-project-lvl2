from gendiff.formatters import stylish, plain, json
from gendiff.diff import create_build
from gendiff.constans import (
    CHILDREN,
    ORIGIN,
    TYPE,
)



def generate_diff(data1, data2, format_name = 'stylish'):
    diff = {
        TYPE: ORIGIN,
        CHILDREN: create_build(data1, data2),
    }
    if format_name == 'stylish':
        res = stylish.render_stylish(diff)
    elif format_name == 'plain':
        res = plain.render_plain(diff)
    else:
        res = json.render_json(diff)
    return res
    