def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    result = []

    def kSum(start, k, curr_sum, curr_nums):
        if k == 2:
            left, right = start, n - 1
            while left < right:
                total = curr_sum + nums[left] + nums[right]
                if total == target:
                    result.append(curr_nums + [nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
            return

        for i in range(start, n - k + 1):
            if i > start and nums[i] == nums[i - 1]:
                continue
            curr_nums.append(nums[i])
            kSum(i + 1, k - 1, curr_sum + nums[i], curr_nums)
            curr_nums.pop()

    kSum(0, 4, 0, [])
    return result
print(fourSum([1, 0, -1, 0, -2, 2], 0))  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
print(fourSum([2, 2, 2, 2, 2], 8))  # Output: [[2, 2, 2, 2]]
print(fourSum([], 0))  # Output: []