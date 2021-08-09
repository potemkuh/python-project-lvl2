from gendiff.formatters import render_stylish, render_plain, render_json


def choice_format(diff, format_name):
    if format_name == 'stylish':
        res = render_stylish.render_stylish(diff)
    elif format_name == 'plain':
        res = render_plain.render_plain(diff)
    elif format_name == 'json':
        res = render_json.render_json(diff)
    return res
