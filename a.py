a = [1,2,3,4,5,6]
b = [1]
mid = len(a)//2
print(a[0:mid])
b.extend(a[0:mid])
print(b)