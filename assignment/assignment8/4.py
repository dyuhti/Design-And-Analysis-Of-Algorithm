num = [2, 4, 0, 9, 6]
r = []

for i in range(len(num)):
    c=0
    for j in range(i+1,len(num)):
        if num[i] < num[j]:
            c += 1
            if c == 2:
                r.append(num[j])
                break
    if c!=2:
        r.append(int("-1"))
print(r)
