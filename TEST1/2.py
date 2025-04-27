num = [3,2,3]
count = 0
ans = 0

for n in num:
    if count == 0:
        ans = n
        if n == ans:
            count+=1
        else:
            count-=1


if count == 1:
    print(ans)
else:
    print("No majority of elements found")