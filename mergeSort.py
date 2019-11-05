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