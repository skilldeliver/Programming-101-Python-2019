class Soul:
    def __init__(self):
        print('Mentally')

    def foo(self):
        return 2


class Body:
    def __init__(self):
        print('Physically')

    def foo(self):
        return 42


class Person(Body, Soul):  # Revert the parent classes
    pass


Person()
