def mapped(*args1, args2 = None):
    args2 = args2 or [2,3,4]
    return list(map(lambda x, y: x * y, *args1, args2))
print(mapped([1,2,3,4]))

def filtered():
    filtered = filter(lambda x: x % 2 == 0, range(10))
    return list(filtered)
print(filtered())
#zip
#Example 1
print(list(zip('Hijacked', range(0,10))))
#Example 2 for same length zips
def assertedZip(xs, ys):
    assert len(xs) == len(ys)
    l = list()
    for x, y in zip(xs, ys):
        print(x,y)
print(assertedZip([1,2,3,4], [2,3,4,5]))



