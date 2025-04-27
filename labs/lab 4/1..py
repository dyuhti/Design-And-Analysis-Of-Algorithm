ar =[1,1,3,3,5,5,7,7]
c=0
for i in range(len(ar)-1):
    if ar[i]+ ar[i+1] in ar:
        c+=2
print(c)