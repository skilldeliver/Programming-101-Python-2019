class A:
    def foo(self):
        print('I am in A')


class B(A):
    pass


class C(A):
    def foo(self):
        print('I am in C')


class D(B, C):
    pass


bar = D()
bar.foo()
# print(D.mro())
