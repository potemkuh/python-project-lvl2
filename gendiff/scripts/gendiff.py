from gendiff.get_args import args
import json
from gendiff.gendiff import generate_diff


def main():
    f1 = json.load(open(args().first_file))
    f2 = json.load(open(args().second_file))
    generate_diff(f1, f2)


if __name__ == '__main__':
    main()