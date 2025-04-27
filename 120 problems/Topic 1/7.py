nums = [3, 7, 3, 5, 2, 5, 9, 2]
l =[]

for i in range(len(nums)):
    if nums[i] not in l:
        l.append(nums[i])

print(l)