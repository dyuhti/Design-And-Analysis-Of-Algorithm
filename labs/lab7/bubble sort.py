ar = [-2, 45, 0, 11, -9]
for i in range(len(ar)):
    for j in range(0,len(ar)-i-1):
        if ar[j]> ar[j+1]:
            temp = ar[j]
            ar[j]=ar[j+1]
            ar[j+1] = temp
print(ar)