def closured():
    x = 25
    print(closured.__closure__)
    print(locals())
    def inner():
        print(locals())
        x = 10
        print(x)
        print(inner.__closure__)
        print(closured.__closure__)
    return inner()

print(closured())

x = 100

def changeScope():
    global x
    x = 50
    y = 20
    def inner():

        nonlocal y
        y = 100
        print(y)
        def underinner():
            y = 150
        underinner()
        print(y)
    print(y)
    return inner()
print(changeScope())
print(x)
changeScope()

def splitter(xs):
    splitter = ' '
    splitter = xs.split(';;;')
    return splitter
print(splitter('hi worlds'))

