def rob(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0], nums[1])

    def rob_helper(nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]

    # Case 1: Rob from first house to second-to-last house
    max1 = rob_helper(nums[:-1])

    # Case 2: Rob from second house to last house
    max2 = rob_helper(nums[1:])

    # Return the maximum of the two cases
    return max(max1, max2)


# Examples
nums1 = [2, 3, 2]  # Output should be 3
nums2 = [1, 2, 3, 1,1]  # Output should be 4

print("Maximum money that can be robbed:", rob(nums1))
print("Maximum money that can be robbed:", rob(nums2))
