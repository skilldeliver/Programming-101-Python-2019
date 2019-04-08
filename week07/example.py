from contextlib import ContextDecorator, contextmanager


class Context(ContextDecorator):
    def __init__(self):
        print('init')
        self.prop = 1

    def __enter__(self):
        print('enter')
        return self

    def __exit__(self, *args):
        print('exit')


@contextmanager
def context():
    print('enter')

    yield 'hi!'

    print('exit')


def generate():
    with context() as cm:
        res = 42
        print('CM instance: ', cm)

    return res


generate()
