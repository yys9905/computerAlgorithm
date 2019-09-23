def selection_sort(array):
    for i in range(len(array)):
        min = i
        for j in range(i, len(array)):
          if array[min] > array[j]:
            min = j
        array[i],array[min] = array[min],array[i]
    return array