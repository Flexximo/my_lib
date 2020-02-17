def adjacentElementsProduct(inputArray):
    m = inputArray[0]*inputArray[1]
    for i in range(0, len(inputArray) - 1):
        m = m if m > inputArray[i]*inputArray[i + 1] else inputArray[i]*inputArray[i + 1]
    return m

print(adjacentElementsProduct([-23, 4, -3, 8, -12]))

