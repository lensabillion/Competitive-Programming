def selectionSort(arr):
    for i in range(0,len(arr)):
        index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[index]:
                index = j
        arr[i],arr[index] = arr[index],arr[i]
        
    return arr
