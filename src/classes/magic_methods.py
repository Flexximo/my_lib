import collections

class Silly:
    def __init__(self):
        self.__dict__["data"] = collections.defaultdict(lambda: 42)
    def __getattr__(self, item):
        return self.data[item]
    def __setattr__(self, key, val):
        val = 11
        self.__dict__[key] = val
    def __delattr__(self, item):
        self.data.pop(item, None)


dict = collections.defaultdict(lambda: 11)
print(dict)
