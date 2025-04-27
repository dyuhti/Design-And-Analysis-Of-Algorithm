nums1 = [2,3,2]
nums2 = [1,2]

a1=0
a2=0
set1 = set(nums1)
set2 = set(nums2)

for num in nums1:
    if num in set2:
        a1+=1
        
for num in nums2:
    if num in set1:
        a2+=1
print([a1,a2])