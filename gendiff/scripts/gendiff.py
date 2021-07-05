from gendiff.get_args import args
import json
import yaml 
from gendiff.gendiff import generate_diff


def main():
    f1 = args().first_file
    f2 = args().second_file
    format = args().format
    if f1.endswith('.json') and f2.endswith('.json'):
        print(generate_diff(json.load(open(f1)), json.load(open(f2)), format))
    if f1.endswith('.yml') and f2.endswith('.yml'):
        print(generate_diff(yaml.safe_load(open(f1)), yaml.safe_load(open(f2)), format))


if __name__ == '__main__':
    main()
