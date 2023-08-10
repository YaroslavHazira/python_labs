def getMin(arr):
    min = arr[0]
    for i in arr:
        if min > i:
            min = i     
    
    return min

minVal = getMin([55, 75, 25, 100])
print(minVal)    