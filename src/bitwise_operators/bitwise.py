def operation(a, b):
    print(a & b)
    print(a | b)
    print(a ^ b)


print(zip('<^>', ['left', 'center', 'right']))

b = [1,2,3,4,5]
for a in b:
    print("") 

width = 5
for n in range(0, 10):
    for base in "dXob":
        print("{0:{width}{base}}".format(n, base=base, width=width))



print("{0:04o}".format(31))




def convert_to_binary(num):
    print(num)
    if num == 0:
        return '1'  
    elif num == 1:
        return '1'
    elif num % 2 == 0:
        return '0' + convert_to_binary(num / 2) 
    else:
        return '1' + convert_to_binary(num - 1)[1:]

def add_binary(a,b):
    return convert_to_binary(a + b)[::-1]

def DecimalToBinary(num): 
      
    if num > 1: 
        DecimalToBinary(num // 2) 
    print(num % 2)


def find_outlier(integers):
    
        if integers[0] % 2 == 0 and integers[len(integers) - 1] % 2 == 0:
            middle = int(len(integers)/2)
            if integers[middle] % 2 != 0:
                return integers[middle]
            elif integers[middle] % 2 == 0:
                return find_outlier(integers.pop(middle))
        elif integers[0] % 2 != 0 and integers[len(integers) - 1] % 2 != 0:
            middle = int(len(integers)/2)
            if integers[middle] % 2 == 0:
                return integers[middle]
            elif integers[middle] % 2 != 0:
                return find_outlier(integers.pop(middle))
        elif integers[0] % 2 == 0 and integers[1] % 2 == 0 and integers[len(integers)-1] % 2 != 0:
                return integers[len(integers)-1]
        else:
                return integers[0]
        # O(1) + O(nlogn)
print(find_outlier([2, 4, 6, 8, 10, 3]))

print(type("a"))

def remove(xs):
    import re
    p = re.compile(r"[A-Za-z]")
    for n in xs:
        if type(n) is str:
            print(n)
            print(re.match(p, n))
            xs.remove(n)
          
    return xs

print(remove([1, 2, "a", 3, "x","c","m","k"]))

import math
