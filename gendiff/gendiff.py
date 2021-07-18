from gendiff.formatters import stylish, plain, json
from gendiff.diff import create_build
import json
import yaml 
from gendiff.constans import (
    CHILDREN,
    ORIGIN,
    TYPE,
)


def generate_diff(f1, f2):
    if f1.endswith('.json') and f2.endswith('.json'):
        print(build_diff(json.load(open(f1)), json.load(open(f2)), format))
    if f1.endswith('.yml') and f2.endswith('.yml'):
        print(build_diff(yaml.safe_load(open(f1)), yaml.safe_load(open(f2)), format))
    

def build_diff(data1, data2, format_name = 'stylish'):
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