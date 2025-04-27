def backtracking_sum_of_subsets(nums):
    def backtrack(index, current_subset, current_sum):
        nonlocal total_sum
        # If we have considered all elements, print the current subset and add the sum to total_sum
        if index == len(nums):
            print(f"Subset: {current_subset}, Sum: {current_sum}")
            total_sum += current_sum
            return

        # Include nums[index] in the current subset
        backtrack(index + 1, current_subset + [nums[index]], current_sum + nums[index])

        # Exclude nums[index] from the current subset
        backtrack(index + 1, current_subset, current_sum)

    total_sum = 0
    backtrack(0, [], 0)
    print(f"Total sum of all subset sums: {total_sum}")
    return total_sum


# Example usage
nums = [1, 2, 3]
backtracking_sum_of_subsets(nums)
