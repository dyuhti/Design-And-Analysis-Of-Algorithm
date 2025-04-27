mat = [[1, 3, 11], [2, 4, 6]]
a=[]
k = 5
c = 0
for i in mat[0]:
    for j in mat[1]:
            a.append(i+j)
a.sort()
print(a[k-1])
