
    
def bubbleSort(array):
    for i in range(len(array)-1):
        finish = True
        for j in range((len(array)-i)-1):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                finish = False
        if (finish == True):
            break
    return array

list = [4,7,1,9,2,3]
print(bubbleSort(list))




