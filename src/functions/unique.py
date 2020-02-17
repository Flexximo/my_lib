def unique(args, seen=set()):
    res = []
    for x in args:
        if x in seen:
            continue
        seen.add(x)
        res.append(x)
    return res

print(unique([1,2,3,4]))
print(unique([1,2,3]))
print(unique([1,2,3,5,8]))
print(unique.__defaults__)

def none(*args, default=None):
    default = default or set()
    a = False or True
    b = True or False
    c = True or True
    d = False or False
    print(default, a,b,c,d)

def get_multiple(*keys, dictio, default=None):
    return [
        dictio.get(key, default)
        for key in keys
    ]
l = {'lemon':'yellow','orange':'orange','apple':'green'}
print(get_multiple('lemon', 'orange', 'main', dictio =l))

def getFromDict(dict, name, default=None):
    data = dict.get(name, default)
l1 = {'a':'b', 'c': 'd'}
print(getFromDict(l, name='a'))

def packed(*args, **kwargs):
    return args, kwargs
args, kwargs = packed(1,23,22, a='b', b='a')
print(args, kwargs)

def packed1(*args, **kwargs):
    return args, kwargs
print(packed1({'a': 'b'}))
print(packed1({0,1,2,3}))
print(packed1(**{'a':'b'}))
none(1,2,3,4)