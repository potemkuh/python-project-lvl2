import argparse

def main():
    parser = argparse.ArgumentParser(description='Generate getdiff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    args = parser.parse_args()
    print(args.first_file, args.second_file)


if __name__ == '__main__':
    main()