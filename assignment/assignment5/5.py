nums =  [5,7,7,8,8,10]
target = 8
ar=[]
for i in range(len(nums)):
    if nums[i]==target:
        ar.append(i)
print(ar)