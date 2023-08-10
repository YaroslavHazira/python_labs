def getMin(arr):
    count = arr[0]
    for i in arr:
        if count > i:
            count = i
        else: 
             count = count     
    print(count)
    


getMin([5098, 6890, 1357,10000])
    