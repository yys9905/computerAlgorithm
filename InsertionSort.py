def sort_process(arr):
    for i in range(1, len(arr)):
        point = i
        a = arr[i]
        while(a < arr[point-1] and point > 0):
            arr[point] = arr[point-1]
            point -= 1
        arr[point] = a 

    return arr

arr = [64, 25, 12, 22, 11]

array = sort_process(arr)
print(array)

