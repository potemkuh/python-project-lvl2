from gendiff.get_parse import get_parse
from gendiff.gendiff import generate_diff


def main():
    args = get_parse()
    first_file = args.first_file
    second_file = args.second_file
    format = args.format
    diff = generate_diff(first_file, second_file, format)
    print(diff)


if __name__ == '__main__':
    main()
