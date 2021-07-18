from gendiff.get_args import args
from gendiff.gendiff import generate_diff


def main():
    f1 = args().first_file
    f2 = args().second_file
    format = args().format
    generate_diff(f1, f2, format)

if __name__ == '__main__':
    main()
