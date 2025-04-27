def intersect(nums1, nums2):
    count1 = {}
    count2 = {}
    for num in nums1:
        if num in count1:
            count1[num] += 1
        else:
            count1[num] = 1
    for num in nums2:
        if num in count2:
            count2[num] += 1
        else:
            count2[num] = 1
    result = []
    for num in count1:
        if num in count2:
            result.extend([num] * min(count1[num], count2[num]))
    return result

# Example usage:
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2))  # Output: [2, 2]

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersect(nums1, nums2))  # Output: [4, 9]