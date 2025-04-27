nums = [1, 2, 1]
num = nums
r = []
sums = 0
d=0
n = len(nums)

# Generate all subarrays of length 1
d = list(set(num))
for i in range(len(d)):
    r.append([d[i]])

# Generate all subarrays of length 2
for i in range(n):
    for j in range(i+1, n):
        a = [nums[i], nums[j]]
        if a not in r and a[::-1] not in r:
            r.append(a)
            if a!= a[::-1]:
                r.append(a[::-1])

r.append(nums)

for subarray in r:
    distinct_count = len(set(subarray))
    sums += distinct_count ** 2
print(r)
print(sums)