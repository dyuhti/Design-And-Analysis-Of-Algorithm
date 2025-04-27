ar=[1,1,3,3,5,5,7,7]
ele = set(ar)
c=0
for x in ar:
    if x+1 in ele:
        c+=1
print(c)