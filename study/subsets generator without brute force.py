nums = [1, 2, 1]
r = []
sum = 0
n = len(nums)

if len(r) <=len(nums):
    for i in range(n):
        r.append([nums[i]])
if len(r) == len(nums):
    for i in range(n):
        for j in range(i+1,n):
            a = [nums[i],nums[j]]
            if a not in r and a[::-1] not in r:
                r.append(a)
                if a != a[::-1]:
                    r.append(a[::-1])
r.append(nums)