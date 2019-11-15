import copy
def make_matrix(o):
    s = [[0 for j in range(len(o[0]))] for i in range(len(o))]
    for i in range(len(o)):
        for j in range(len(o[i])):
            if (i == 0 and j == 0):
                pass
            elif (i == 0):
                s[i][j] = o[i][j] + s[i][j-1]
            elif (j == 0):
                s[i][j] = o[i][j] + s[i-1][j]
            else:
                s[i][j] = o[i][j] + max(s[i-1][j], s[i][j-1])
    return s

def solution(o,s):
    i = len(o)-1
    j = len(o[0])-1
    result = []
    for a in range(len(o)*2 -1):
        result.append(o[i][j])
        if s[i-1][j]> s[i][j-1] or j == 0:
            i -= 1
        else:
            j -= 1
    result.reverse()
    return result
    
o = [[6,7,12,5],
[5,3,11,18],
[7,17,3,3],
[8,10,14,9]]

print(solution(o, make_matrix(o)))