def optimal_subset_sum(nums, target):
    n = len(nums)
    closest_sum = 0

    # Iterate through all possible subsets
    for i in range(1 << n):  # 2^n subsets
        subset_sum = 0

        # Generate each subset
        for j in range(n):
            if i & (1 << j):  # Check if the j-th element is included in the subset
                subset_sum += nums[j]

        # Update the closest sum if the current subset sum is <= target
        if subset_sum <= target:
            closest_sum = max(closest_sum, subset_sum)

    return closest_sum


# Example usage:
nums = [3, 1, 4, 1, 5]
target = 7
optimal_cost = optimal_subset_sum(nums, target)
print(f"The optimal subset sum closest to {target} is: {optimal_cost}")
