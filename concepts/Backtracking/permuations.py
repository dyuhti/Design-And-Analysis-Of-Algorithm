def permutations(nums):
    result = []

    def backtrack(current_permutation, remaining_nums):
        if len(current_permutation) == len(nums):
            result.append(current_permutation[:])  # Make a copy of the permutation
            return

        for num in remaining_nums:
            current_permutation.append(num)
            new_remaining = remaining_nums[:]
            new_remaining.remove(num)
            backtrack(current_permutation, new_remaining)
            current_permutation.pop()

    backtrack([], nums)
    return result


# Example usage:
nums = [1, 2, 3]
perms = permutations(nums)
print("All permutations:", perms)
