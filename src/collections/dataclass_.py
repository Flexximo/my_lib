from dataclasses import dataclass
from collections import defaultdict
@dataclass(frozen=True) # Sets field mutable or not
class Programmer:
    name: str
    lang: str
    age: int = 18

args = [1,1,23,4]
dictio = { }
e = dictio.setdefault('a', []).append(args)
print(dictio)
d = dictio.get('a')
print(d)

def count_words(text="Son of Ra is god as well"):
    res = defaultdict(lambda: 0)
    for word in text.split():
        res[word] += 1
    print(res)

word = "word"
print("{:<9}".format(12323))

def fun(arg=None):
    print(arg**arg)

fun(22)
