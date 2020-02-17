import functools

class Proxy:
    def __init__(self, cls, obj):
        self.__cls = cls
        self.__obj = obj
    def __getattr__(self, item):
        item = getattr(self.__cls, item)
        if callable(item):
            return functools.partial(item, self.__obj)
        return item

def _super(cls, obj):
    mro = type(obj).mro()
    super_cls = mro[mro.index(cls) + 1]
    return Proxy(super_cls, obj)

class Base:
    def foo(self):
        print("Base class")

class A(Base):
    def foo(self):
        print("A")
        _super(A, self).foo()

class B(Base):
    def foo(self):
        print("B")
        _super(B, self).foo()

class C(A, B):
    pass


c = C()
print(_super(A, C()))
print(c.foo())
