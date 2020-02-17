def printAll(*args, default=None):
    for x in args:
        print(x)
    print(default)
    return 0

if __name__ == '__main__':
    printAll(1,2,3,4, default = 10 )