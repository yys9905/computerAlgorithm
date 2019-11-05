given_array = ["a","b","c"]

def fb(given_array):
    fb_al(given_array, [], 0)

def fb_al(given_array, result, depth):
    if len(given_array) != depth:
        fb_al(given_array,result,depth+1)
        result.append(given_array[depth])
        fb_al(given_array,result,depth+1)
        result.pop()
    else:
        print(result)
        
            

fb(given_array)
