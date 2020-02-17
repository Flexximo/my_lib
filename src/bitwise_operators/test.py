

# def mutateTheArray(n, a):
#     out = [0]*n
#     j = 0
#     for i in range(-1, n):
#         # out.append(a[i] + a[i + 1] + a[i + 2]) if i > -1 else out.append(0 + a[i + 1] + a[i + 2])
#         if i > - 1 and i <= n - 3:
#             print(i)
#             j = j + 1
#             out[j] = a[i] + a[i + 1] + a[i + 2]
#         elif i == -1:
#             print(a[i+1], a[i+2])
#             out[j] = a[i + 1] + a[i + 2]
#         elif i == n - 2:
#             j = j + 1
#             out[j] = a[i] + a[i + 1]
#     return out
# print(mutateTheArray(5, [1,2,3,4,5]))

# def filt(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False

# [3, 6, 9, 12, 9]

# def iq_test(numbers):
#     even = []
#     odd = []
#     enum = list(enumerate(numbers.split()))
#     for i in enum:
#         if int(i[1]) % 2 == 0:
#             even.append((i[0] + 1, i[1]))
#             print(even[0][1])
#         elif int(i[1]) % 2 != 0:
#             odd.append((i[0] + 1, i[1]))
#             print(odd)

# print(iq_test("1 2 3 4 5 6 7"))



# def shapeArea(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return (4 * (n - 1)) + shapeArea(n-1) + (4 * (n - 2)) + shapeArea(n- 2)



# def countTinyPairs(a, b, k):
#     counter = 0
#     arr = [0]*len(a)
#     for x in range(0, len(a)):
#         arr[x] = (a[x], b[(len(b) - 1) - x])
#     for t in arr:
#         if int(str(t[0] + t[1])) < k:
#             counter = counter + 1
#             print(counter)
#     return counter
# countTinyPairs([1,2,3], [1,2,3], 32)

# def almostIncreasingSequence(sequence):
#     counter = 0

#     s = sequence
#     s.sort()

#     if len(s) == 1 or len(s) == 2:
#         return True
#     else:
#         for x in range(0, len(s)):
#             for y in range(len(s) - 1, 0, -1):
#                 if s[x] == s[y]:
#                     counter = counter + 1
#     if len(s) % 2 == 0:
#         if counter % 2 != 0:
#             return False
#         else:
#             return True
#     else:
#         if counter % 2 == 0:
#             return False
#         else:
#             return True
# print(almostIncreasingSequence([1, 3, 2, 1]))

def almostIncreasingSequence(sequence):
    tochangesequence = sequence
    def checkforduplicate(element):
        counter = 0
        value = None
        for i in range(0, len(sequence)):
            if sequence[element] == sequence[i]:
                counter = counter + 1
                if counter > 1:
                    value = i
                    break
                else:
                    print("I am here")
                    return None
        return value

    for i in range(0, len(tochangesequence)):
        if checkforduplicate(i):
            tochangesequence.pop(checkforduplicate(i))
            return tochangesequence
    print(tochangesequence)


almostIncreasingSequence([1,2,3,4,1,1,1])

def digitDegree(n):
    import math
    count = 0
    sum_ = 0
    if n > 10:
        sum_ = sum([int(i) for i in str(n)])
        count = count + 1
        if sum_ > 10:
            return count + digitDegree(sum_)
        else:
            return count
    elif n < 10:
        if count > 0:
            return count
        else:
            return 0
    elif n == 10:
        if count > 0:
            return count
        else:
            return 1
print(digitDegree(133121))

def howManySundays(n, startDay):
    week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    start = week.index(startDay)
    print(start)
    # end = (len(week) - start) - 1
    # new = week[start:] + week[:start]
    count = 0
    total = n//7
    n = n % 7
    print(n)
    if n + start > 6:
        total = total + 1
    print(total)
    return total


howManySundays(9, "Saturday")
#
# def chartFix(chart):
#     updated = chart
#     for i in range(0, len(chart) - 1):
#         for j in range(1, len(chart) - 1):
#             if i == 0:
#                 if chart[i] >= chart[j]:
#                     updated.pop(i)
#             else:
#                 if chart[i] >= chart[j] and chart[i] < chart[j + 1]:
#                     updated.pop(j)
#     return updated


def isArithmeticProgression(sequence):
    diff = sequence[1] - sequence[0]
    for i in range(len(sequence),0,-1):
        if sequence[i] - sequence[i - 1] > diff or sequence[i] - sequence[i - 1] < diff:
            return False
        else:
            pass
    return True
#
# print(chartFix([1, 3, 4, 1, 8, 9, 3, 5]))


class Config():
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.command = lambda: self.function()
    def function(self):
        return self.name, self.id


config = Config("config", 0)
print(config.command())
