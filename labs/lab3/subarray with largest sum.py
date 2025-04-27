def max_subarray_sum(nums):
    """
    Find the subarray with the largest sum in the given array.

    Args:
        nums (list): A list of integers representing the input array.

    Returns:
        int: The maximum subarray sum.
    """
    # Initialize max_sum and current_sum with the first element of the array
    max_sum = nums[0]
    current_sum = nums[0]

    for num in nums[1:]:
        # Update current_sum to be the maximum of:
        # 1. The current element (num)
        # 2. The sum of the current element and the previous current_sum
        current_sum = max(num, current_sum + num)

        # Update max_sum to be the maximum of:
        # 1. The current max_sum
        # 2. The current_sum
        max_sum = max(max_sum, current_sum)

    return max_sum


# Example usage
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = max_subarray_sum(nums)
print(f"The maximum subarray sum is: {result}")