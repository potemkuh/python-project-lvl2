from gendiff.build_diff import build_diff
import json
import yaml 
from gendiff.constans import (
    CHILDREN,
    ORIGIN,
    TYPE,
)


def generate_diff(f1, f2, format='stylish'):
    if f1.endswith('.json') and f2.endswith('.json'):
        result = build_diff(json.load(open(f1)), json.load(open(f2)), format)
    if f1.endswith('.yml') and f2.endswith('.yml'):
        result = build_diff(yaml.safe_load(open(f1)), yaml.safe_load(open(f2)), format)
    return result 
