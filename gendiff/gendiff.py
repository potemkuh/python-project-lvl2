from gendiff.diff import build_diff
from gendiff.format import choice_format
import json
import yaml


def format_selection(data1, data2):
    if data1.endswith('.json') and data2.endswith('.json'):
        return json.load(open(data1)), json.load(open(data2))

    if data1.endswith('.yml') and data2.endswith('.yml'):
        return yaml.safe_load(open(data1)), yaml.safe_load(open(data2))


def generate_diff(first_file, second_file, format='stylish'):
    part = format_selection(first_file, second_file)
    print(part)
    diff = build_diff(part[0], part[1])
    return choice_format(diff, format)
