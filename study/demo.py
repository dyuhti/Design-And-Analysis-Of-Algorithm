nums = [1, 2, 1]
r = []
sums = 0

n = len(nums)

# Generate all subarrays
for i in range(n):
    for j in range(i, n):
        subarray = nums[i:j+1]
        if subarray not in r:
            r.append(subarray)

# Calculate the sum
for subarray in r:
    distinct_count = len(set(subarray))
    sums += distinct_count ** 2

print(r)
print(sums)