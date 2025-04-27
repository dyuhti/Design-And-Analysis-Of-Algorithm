def subset_sum(nums, target):
    result = []

    def backtrack(start, current_subset, current_sum):
        if current_sum == target:
            result.append(current_subset[:])  # Make a copy of the subset
            return
        if current_sum > target:
            return

        for i in range(start, len(nums)):
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset, current_sum + nums[i])
            current_subset.pop()

    backtrack(0, [], 0)
    return result


# Example usage:
nums = [2, 3, 5, 7, 8]
target = 10
subsets = subset_sum(nums, target)
print(f"All subsets with sum {target}: {subsets}")
