nums = [1,1,2]
ar =[]
underscore = "_"
for i in range(len(nums)):
    if i+1 <= len(nums)-1:
        if nums[i] == nums[i+1] :
            if nums[i] is not  ar:
                ar.append(str(nums[i]))
                ar.append(underscore)
    else:
        ar.append(str(nums[i]))

print(sorted(ar))
n=[]
for i in range(len(ar)):
    if ar[i] != "_":
        n.append(ar[i])
print(len(n))

