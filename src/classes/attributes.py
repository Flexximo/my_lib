class Counter:
    all_counters = []
    def __init__(self, initial_count=0):
        Counter.all_counters.append(self)
        self.count = initial_count


c1 = Counter(100)
print(c1.__class__)
print(c1.__dict__)
c1.__dict__["id"] = 123456
print(c1.__dict__["count"] == c1.count)
print(c1.__dict__)

print(Counter.__name__, Counter.__doc__, Counter.__module__, Counter.__class__, Counter.__bases__ )
print(Counter.__dict__)

c2 = Counter(200)

print(c1.all_counters)
assert len(Counter.all_counters) == 2
assert c1.all_counters is c2.all_counters



class Numbers:
    def __init__(self, numb):
        self.numb = numb
    def get_num(self):
        return self.numb

n = Numbers(10)
print(n.get_num())
print(Numbers.get_num(n))
print(n.__class__.get_num(n))
print(type(n).get_num(n))
print(n.__dict__)

class A:
    __slots__ = ["x", "y"]
