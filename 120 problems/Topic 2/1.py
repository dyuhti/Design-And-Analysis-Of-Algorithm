nums =[-5, -1, -3, -2, -4]

for i in range(len(nums)):
    for j in range(len(nums)-i-1):
        if nums[j]>nums[j+1]:
            temp =nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp
print(nums)