def chain(iterable_one, iterable_two):
    for el1 in iterable_one:
        yield el1

    for el2 in iterable_two:
        yield el2


def chain2(iterable_one, iterable_two):
    result = []

    for el1 in iterable_one:
        result.append(el1)

    for el2 in iterable_two:
        result.append(el2)

    return result


def chain3(iterable_one, iterable_two):
    iterable_one = list(iterable_one)
    iterable_one.extend(iterable_two)

    return iterable_one


def chain4(iterable_one, iterable_two):
    return list(iterable_one) + list(iterable_two)


class Chain:
    def __init__(self, iter1, iter2):
        self.index = 0
        self.iter1 = iter1
        self.iter2 = iter2

    def __iter__(self):
        return self

    def __next__(self):
        index = self.index
        self.index += 1

        try:
            return self.iter1[index]
        except IndexError:
            try:
                return self.iter2[index - len(self.iter1)]
            except IndexError:
                raise StopIteration()


def chain5(iterable_one, iterable_two):
    yield from iterable_one

    for el in iterable_one:
        yield el


iterable1 = [1, 2, 3]
iterable2 = ('Ivo', 'Pavli')

for element in chain5(iterable1, iterable2):
    print(element)
