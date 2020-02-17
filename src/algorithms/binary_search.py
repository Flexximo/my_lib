def bi_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int(low + high / 2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

def bi_search_rec(array, key, left, right): #Рекурсивно
    mid = int(left + (right - left) / 2)
    print(mid)
    if array[mid] == key:
        return mid
    elif array[mid] > key:
        return bi_search(array, key, left, mid - 1)
    else:
        return bi_search_rec(array, key, mid + 1, right)

def bi_search_iterative(array, key): #Итеративно
    left = 0
    right = len(array)
    operation = 0
    while(left <= right):
        mid = int(left + right / 2)
        if array[mid] == key:
            return mid
        elif array[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
        operation = operation + 1
        print(operation, "times")

def custom(array, mid, left=0, right=0, key=4):
    left = left or (mid - mid) #len(array) - len(array)
    right = right or len(array)
    if array[mid] == key:
        return mid
    elif array[mid] > key:
        left = mid - 1
    else:
        right = mid + 1




def bi_search_rec_flagged(array, key, left, right):
    mid = left + (right - left) / 2

def fib(n):
    if n < 0:
        return "not exist"
    elif n < 1:
        return 0
    elif n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n-2)

if __name__ == "__main__":
    print(bi_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))
    print(bi_search_rec([10, 20, 30, 40, 50, 100], 30, 0, 3))
    print(custom([1, 2, 3, 4, 5, 6], 3))
    print(bi_search_iterative([1,2,3, 4, 5, 6, 7, 8, 9, 10], 2))
    print(fib(10))

