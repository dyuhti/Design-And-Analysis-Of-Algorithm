nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
c=0
ans=0
for i in range(len(nums)):
    if nums[i]==target:
        c=1
        ans=i
        break
if c==0:
    print("-1")
else:
    print(ans)