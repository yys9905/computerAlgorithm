def make_matrix(x,y):
    s = [[0 for j in range(len(y)+1)] for i in range(len(x)+1)]
    hm = [["" for i in range(len(y)+1)]]
    h = ""
    for i in range(len(x)):     
        temp = [""]
        for j in range(len(y)):
            if x[i] == y[j]:
                s[i+1][j+1] = s[i][j] +1
                h = "c"
            elif s[i][j+1] > s[i+1][j]:
                s[i+1][j+1] = s[i][j+1]
                h = "u"
            elif s[i][j+1] < s[i+1][j]:
                s[i+1][j+1] = s[i+1][j]
                h = "l"
            else:
                s[i+1][j+1] = s[i][j+1]
                h = "ul"
            temp.append(h)
        hm.append(temp)
    return s, hm
    
def solution(x,s,hm):
    locI = len(s)-1
    locJ = len(s[0])-1
    print(s[locI][locJ])
    sol(x, s,hm,locI, locJ, [])

def sol(x, s, hm, locI, locJ,array):
    h = hm[locI][locJ]
    if h != "":
        if h == "ul":
            sol(x, s,hm,locI-1,locJ,array)
            sol(x, s,hm,locI,locJ-1,array)
        elif h == "u":
            sol(x, s,hm,locI-1,locJ,array)
        elif h == "l":
            sol(x, s,hm,locI,locJ-1,array)
        elif h == "c":
            array.append(x[locI-1])
            sol(x, s,hm,locI-1,locJ-1,array)
            array.pop()
            
    else:
        print(array)

x = ["A","B","C","B","D","A","B"]
y = ["B","D","C","A","B","A"]

s, hm = make_matrix(x,y)
solution(x, s,hm)