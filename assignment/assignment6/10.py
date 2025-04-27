def countSubarraysWithMedianK(nums, k):
    n = len(nums)
    count = 0

    for i in range(n):
        # Expand window to the left until median is no longer k
        left = i
        while left >= 0 and nums[left] == k:
            left -= 1
            count += 1

        # Expand window to the right until median is no longer k
        right = i + 1
        while right < n and nums[right] == k:
            right += 1
            count += 1

    return count


# Example usage
nums = [2, 3, 1, 4]
k = 2
print(countSubarraysWithMedianK(nums, k))  # Output: 1
