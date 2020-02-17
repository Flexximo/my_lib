

class CustomException(Exception):
    pass


def coroutine(fun):
    def inner(*args, **kwargs):
        g = fun(*args, **kwargs)
        g.send(None)
        return g
    return inner


def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            break
        else:
            print("...", message)
    return "From subgen()"

@coroutine
def delegator(g):
    result = yield from g
    print(result)
