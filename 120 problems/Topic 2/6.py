nums = [1,2,3,1]

for i in range(1,len(nums)):
    if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
        print(i)
        break