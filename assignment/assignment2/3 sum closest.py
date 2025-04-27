def threeSumClosest(nums, target):
    nums.sort()  # Sort the input list
    closest_sum = nums[0] + nums[1] + nums[2]  # Initialize with the sum of the first three elements

    for i in range(len(nums) - 2):
        # Skip duplicates for the first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == target:
                return target  # If the sum equals the target, return it

            if abs(total - target) < abs(closest_sum - target):
                closest_sum = total  # Update the closest sum if the current sum is closer

            if total < target:
                left += 1
            else:
                right -= 1

    return closest_sum

print(threeSumClosest([-1, 2, 1, -4], 1))  # Output: 2
print(threeSumClosest([0, 0, 0], 1))  # Output: 0
print(threeSumClosest([1, 1, 1, 0], -100))  # Output: 2