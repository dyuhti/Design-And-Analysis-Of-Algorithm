def Triplets(nums):
    n = len(nums)
    count = 0

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                    count += 1

    return count


# Example usage:
nums = [1, 2, 3, 4]
result = Triplets(nums)
print("Number of unequal triplets:", result)  # Output: 4
