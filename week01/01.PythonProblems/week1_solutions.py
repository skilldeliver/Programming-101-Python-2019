def g(arg):
    return arg


def p(arg):
    return True


def f(args):
    result = []

    for arg in args:
        if p(arg):
            result.append(g(arg))

    return result


def ff(args):
    """
    Same as f, but uses list comprehension.
    """
    return [g(arg) for arg in args if p(arg)]


def to_digits(n):
    n = abs(n)

    return [int(ch) for ch in str(n)]


def sum_of_digits(n):
    return sum(to_digits(n))


def join(items, delimiter):
    """
    Used ''.join() instead.

    This is just an example implementation.
    """
    result = ''
    n = len(items)

    for index in range(n):
        item = items[index]

        result = result + item

        if index != n - 1:
            result += delimiter

    return result


def to_number(digits):
    chars = [str(digit) for digit in digits]

    return int(join(chars, ''))


def fact(n):
    if n in [0, 1]:
        return 1

    result = 1

    for x in range(n):
        result *= x + 1

    return result


def fact_digits(n):
    return sum([fact(digit) for digit in to_digits(n)])


def char_histogram(string):
    result = {}

    for ch in string:
        if ch not in result:
            result[ch] = 0

        result[ch] += 1

    return result
