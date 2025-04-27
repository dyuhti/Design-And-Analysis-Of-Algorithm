nums = [3, 1, 2, 2, 2, 1, 3]
k = 2
c=0

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if (i*j) % k == 0 :
            if nums[i] == nums[j]:
                c+=1
print(c)