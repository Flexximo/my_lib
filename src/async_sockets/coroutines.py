

def subgen():
    x = 'Ready to accept message'
    message = yield x
    print("Subgen received:", message)


class CustomException(Exception):
    pass


def coroutine(fun):
    def inner(*args, **kwargs):
        g = fun(*args, **kwargs)
        g.send(None)
        return g
    return inner


@coroutine
def average():
    count = 0
    summ = 0
    average = None
    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
            break
        except CustomException:
            print("CustomException")
            break
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)
    return average

def pow():
    init = -1
    number = None
    while True:
        try:
            x = yield number
        except StopIteration:
            return
        else:
            number = x**init

def averagecopy(x):
    count = 0
    summ = 0
    average = None
    while True:
        try:
            yield average
        except StopIteration:
            print('Done')
            break
        except CustomException:
            print("CustomException")
            break
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)
    return average
