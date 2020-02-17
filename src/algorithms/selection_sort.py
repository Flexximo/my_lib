def sorted(array):
    first = array[0]
    first_index = 0
    sorted = []
    for i in range(1, len(array)):
        if array[i] < first:
            first = array[i]
            first_index = i
            sorted.append(array)




def smaller_element(array):
    smallest = array[0]
    smallest_index = 0
    array_sorted = []
    for i in range(1, len(array)):
        if smallest > array[i]:
            smallest = array[i]
            smallest_index = i
            array_sorted.append(smallest_index)
            smaller_element(array.pop[array[i]])
    return smallest_index

def selectionSort(array):
    newArr = []
    for i in range(len(array)):
        smallest = smaller_element(array)
        newArr.append(array.pop(smallest))
    return newArr

if __name__ == "__main__":
    print(selectionSot([1,4,5,6,8,2,5]))
