from time import time

def gen(s):
    for char in s:
        yield char


def gen_filename():
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time() * 1000)
        yield pattern.format(str(t))


def gen1(s):
    for char in s:
        yield char


def gen2(n):
    for i in range(n):
        yield i

g1 = gen1("Dmitriy")
g2 = gen2(7)

tasks = [g1, g2]

while True:
    task = tasks.pop(0)
    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass
