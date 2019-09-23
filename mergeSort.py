def mergeSort(list):
    left = []
    right = []
    if len(list) <= 1:
        return list
    else:
        middle = int(len(list)/2)
        left = list[0:middle]
        right = list[middle:]
        # for i in range(middle):
        #     left.append(list[i])
        # for i in range(middle,len(list)):
        #     right.append(list[i])
        left = mergeSort(left)
        right = mergeSort(right)
        return merge(left, right)

def merge(left, right):
    result = []
    while(len(left) > 0 and len(right) > 0):
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if len(left) > 0:
        result.extend(left)
        # for i in left:
        #     result.append(i)
    else:
        result.extend(right)
        # for i in right:
        #     result.append(i)
    return result

def sort_process(arr):
    for i in range(1, len(arr)):
        point = i
        a = arr[i]
        while(a < arr[point-1] and point > 0):
            arr[point] = arr[point-1]
            point -= 1
        arr[point] = a 

    return arr

import random
import time

n = 100000

unordered = []
for i in range(n):
    num = random.randint(1,n)
    unordered.append(num)

start = time.time()
sort_process(unordered.copy())
end = time.time()
inse = end - start
print(inse)
print("end")

start = time.time()
mergeSort(unordered.copy())
end = time.time()
mer = end - start
print(mer)
print("end")

print(inse / mer)