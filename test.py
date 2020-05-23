class A(object):
    pass


class B(A):
    pass


class C(B):
    pass

class D(object):
    pass

a = A()
b = B()
c = C()

res1 = isinstance(C, A)
print(res1)
res2 = isinstance(c, A)
print(res2)
res3 = isinstance(c, D)
print(res3)


