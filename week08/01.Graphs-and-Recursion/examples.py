def fact_rec(n):
    if n > 1:
        return n * fact_rec(n - 1)

    return 1


def fact_iter(n):
    def tail_rec(product, counter, max_count):
        if (counter > max_count):
            return product

        return tail_rec(product * counter, counter + 1, max_count)

    return tail_rec(1, 1, n)


print('Recursive: ', fact_rec(10))
print('Iterative: ', fact_iter(10))
