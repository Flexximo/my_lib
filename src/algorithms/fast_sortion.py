def sort(array):
    if len(array) < 2:
        return array
    else:

        x = 5
        y = 6
        print([y]+[x])
        center = array[0]
        left = [i for i in array[1:] if i <= array[0]]
        right = [i for i in array[1:] if i > array[0]]
        print([center])
        return sort(left) + [center] + sort(right)

if __name__ == "__main__":
    print(sort([1,2,5,9,20,88,3,1,1,1,15]))

