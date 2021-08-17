from gendiff.diff import build_diff
from gendiff.format import choice_format
import json
import yaml


def format_selection(file):
    if file.endswith('.json'):
        return json.load(open(file))

    if file.endswith('.yml'):
        return yaml.safe_load(open(file))


def generate_diff(first_file, second_file, format='stylish'):
    data1 = format_selection(first_file)
    data2 = format_selection(second_file)
    diff = build_diff(data1, data2)
    return choice_format(diff, format)
