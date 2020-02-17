from random import randrange
from time import time


queue = []

def print_time():
    while True:
        t0 = time()
        count = 0
        if count % 10 == 0:
            print(time() - t0)
        yield


def gen_random():
    while True:
        num = randrange(1000)
        print(num)
        time.sleep(1)
        yield


def main():
    while True:
        gen = queue.pop(0)
        next(gen)
        queue.append(gen)


if __name__ == "__main__":
    g1 = print_time()
    g2 = gen_random()
    queue.append(g1)
    queue.append(g2)
    main()
