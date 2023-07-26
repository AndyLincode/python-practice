# type()
print(type("hello"))  # <class 'str'>
print(type("hello") == type("goodbye"))  # True
print(type("hello") == type(5))  # False

#  isinstance(obj, class)


class C:
    pass


class B(C):
    pass


class A(B):
    pass


a = A()
b = B()
c = C()

print(isinstance(a, A))  # True
print(isinstance(a, B))  # True
print(isinstance(a, C))  # True
print(isinstance(c, A))  # False
print(issubclass(A, A))  # True
print(issubclass(A, B))  # True
print(issubclass(A, C))  # True
print(issubclass(C, A))  # False
