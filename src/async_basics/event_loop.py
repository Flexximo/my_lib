from time import time
from collections import deque
from tornado.ioloop import IOLoop

current = deque()

class sleep(object):
    def __init__(self, timeout):
        self.deadline = time() + timeout
    def __await__(self):
        def switch_to(coroutine):
            current.append(coroutine)
            coroutine.send(time())
        IOLoop.instance().add_timeout(self.deadline, switch_to, current[0])
        current.pop()
        return (yield)

def coroutine_start(run, *args, **kwargs):
    coroutine = run(*args, **kwargs)
    current.append(coroutine)
    coroutine.send(None)


# if __name__ == "__main__":
#     async def hello(name, timeout):
#         while True:
#             now = await sleep(timeout)
#             print("Hello, {}!\tts:{}".format(name, now))
#     coroutine_start(hello, "friends", 2.5)
#     coroutine_start(hello, "world", 3.5)
#     IOLoop.instance().start()


def cor():
    x = yield
    yield x
g = cor()
g.send(None)
print(g.send(1))
