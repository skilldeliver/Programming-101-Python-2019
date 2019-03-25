class A:
    def foo(self):
        print('I am in A')


class B(A):
    # SECOND: Try delete this method and see what happens
    def foo(self):
        print('I am in B')


class C(A):
    def foo(self):
        print('I am in C')


class D(B, C):
    # FIRST: Try delete this method and see what happens
    def foo(self):
        print('I am in D')


bar = D()
bar.foo()
