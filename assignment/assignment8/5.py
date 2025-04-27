nums = [1,3,6,10,12,15]
s=0
c=0

for i in range(len(nums)):
    if nums[i]%2==0 and nums[i]%3 ==0:
        s+=nums[i]
        c+=1

print(int(s/c))
