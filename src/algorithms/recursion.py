def sum(array): #сумма всех эл-в массива

    if len(array) <= 0:
        return 0
    return array.pop(0) + sum(array)



def mTable(x, y):
    if x == 1 and y == 1:
        return x * y
    else:
        return


def countItems(array, counter): #кол-во элементов в массиве
    if counter == len(array):
        return counter
    else:
        return countItems(array, counter + 1)

def findBig(array, next, num): #самый большой член массива
   if next == len(array):
       return num
   elif num < array[next]:
       num = array[next]
       return findBig(array, next + 1, num)
   elif num > array[next]:
       return findBig(array, next + 1, num)


def binarySearch(array, start, end, value):
    if start >= 0 and start < end:
        middle = int((start + end) / 2)
        if array[middle] == value:
            return middle
        elif array[middle] < value:
            return binarySearch(array, middle + 1, end, value)
        else:
            return binarySearch(array, start, middle - 1, value)


def quickSort(array):
    if len(array) <= 1:
        return array
    else:
        center = array[0]
        left = [n for n in array[1:] if n <= center]
        right = [n for n in array[1:] if n > center]
        return quickSort(left) + [center] + quickSort(right)






if __name__ == "__main__":
    print(sum([1, 2, 3, 4, 5, 6]))
    print(countItems([1,2,3,4,5], 0))
    print(findBig([4, 22, 3, 2, 224, 10000, 48, 250], 0, 0))
    print(binarySearch([1, 8, 22, 44, 55, 77, 88], 0, 7, 55))
    print(quickSort([1, 3, 7,11, 22, 25, 88]))

