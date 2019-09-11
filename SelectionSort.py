
def find_min_index(list):
    minIndex = 0

    for pointerIndex in range(1,len(list)):
        if list[minIndex] > list[pointerIndex]:
            minIndex = pointerIndex
    return minIndex

def swap(arr, min, border):
    temp = arr[min]
    arr[min] = arr[border]
    arr[border] = temp
    return arr
    
def sort_process(arr):
    for borderIndex in range(len(arr)-1):
        min = borderIndex + find_min_index(arr[borderIndex:])
        arr = swap(arr, min , borderIndex)
    return arr

arr = [64, 25, 12, 22, 11]

array = sort_process(arr)
print(array)