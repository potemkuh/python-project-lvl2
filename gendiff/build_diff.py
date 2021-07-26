from gendiff.diff import create_build
from gendiff.formatters import render_stylish, render_plain, render_json
from gendiff.constans import (
    CHILDREN,
    ORIGIN,
    TYPE,
)


def build_diff(data1, data2, format_name='stylish'):
    diff = {
        TYPE: ORIGIN,
        CHILDREN: create_build(data1, data2),
    }
    if format_name == 'stylish':
        res = render_stylish.render_stylish(diff)
    elif format_name == 'plain':
        res = render_plain.render_plain(diff)
    elif format_name == 'json':
        res = render_json.render_json(diff)
    return res
