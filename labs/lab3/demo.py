def max_subarray_sum_circular(nums):
    # Helper function to find maximum subarray sum using Kadane's algorithm
    def kadane_max_subarray(arr):
        max_ending_here = max_so_far = arr[0]
        for x in arr[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    # Helper function to find minimum subarray sum using Kadane's algorithm
    def kadane_min_subarray(arr):
        min_ending_here = min_so_far = arr[0]
        for x in arr[1:]:
            min_ending_here = min(x, min_ending_here + x)
            min_so_far = min(min_so_far, min_ending_here)
        return min_so_far

    total_sum = sum(nums)  # Step 3: Total sum of the array
    max_kadane = kadane_max_subarray(nums)  # Step 1: Max subarray sum (non-wrapping)
    min_kadane = kadane_min_subarray(nums)  # Step 2: Min subarray sum (for wrapping)

    # Step 4: Max subarray sum (wrapping)
    max_wraparound = total_sum - min_kadane

    # Step 5: Handle edge case where all elements are negative
    if max_wraparound == 0:
        return max_kadane

    # Step 6: Return the maximum of both cases
    return max(max_kadane, max_wraparound)


# Example usage
nums = [1, -2, 3, -2]
print(max_subarray_sum_circular(nums))  # Output: 3

nums = [5, -3, 5]
print(max_subarray_sum_circular(nums))  # Output: 10

nums = [-3, -2, -3]
print(max_subarray_sum_circular(nums))  # Output: -2