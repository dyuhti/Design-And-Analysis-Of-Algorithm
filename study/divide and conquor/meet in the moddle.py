a=[6,8,12,14,7]
key=21
n=len(a)
for i in range(n-1):
    y=0
    m=[]
    x=a[i]
    c=[]
    c.append(a[i])
    for j in range(i+1,n):
        x+=a[j]
        c.append(a[j])
        if x<=key:
            if y<=x:
                m=c
                y=x
print(m,y)