class X:
    pass


class Y:
    pass


class Z:
    pass


class A(X, Y):
    pass


class B(Y, X):  # Change Z to X
    pass


class M(A, Z):  # Switch B and A
    pass


from pprint import pprint
pprint(M.mro())
