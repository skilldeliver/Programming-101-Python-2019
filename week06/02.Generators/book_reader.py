from os import listdir
from os.path import isfile, join


def get_next_row(path):
    for file_ in listdir(path):
        if isfile(join(path, file_)):
            file_path = '{}/{}'.format(path, file_)

            with open(file_path) as f:
                for line in f:
                    yield line


def format_chapter(lines_list):
    return ''.join(lines_list)


def get_chapters():
    initial = True
    result = []

    for row in get_next_row('Book'):
        if row.startswith('# Chapter'):
            if initial:
                initial = False
                result.append(row)
                continue

            yield format_chapter(result)
            result = []

        result.append(row)

    yield format_chapter(result)


def main():
    generator = get_chapters()

    while True:
        input_ = input('Press enter: ')

        if input_ == '':
            try:
                print(next(generator))
            except StopIteration:
                print('That\'s all folks.')
                break


if __name__ == '__main__':
    main()
