from gendiff.get_parse import get_parse
from gendiff.gendiff import generate_diff


def main():
    first_file = get_parse().first_file
    second_file = get_parse().second_file
    format = get_parse().format
    diff = generate_diff(first_file, second_file, format)
    print(diff)


if __name__ == '__main__':
    main()
