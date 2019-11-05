def quickSort(array):
    p,q= 0,0
    r = len(array)-1

    for i in range(r):
        if array[r] < array[i]:
            pass
        else:
            array[q], array[i] = array[i], array[q]
            q += 1
    array[q],array[r] = array[r],array[q]

    if len(array[:q]) > 1:
        array[:q] = quickSort(array[:q])
    if len(array[q+1:]) > 1:
        array[q+1:] = quickSort(array[q+1:])
    return array

array = [9,7,5,11,12,2,14,3,10,6]
print(quickSort(array))
