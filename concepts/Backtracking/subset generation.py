def generate_subsets(nums):
    def backtrack(index, current_subset):

        print(current_subset)

        for i in range(index, len(nums)):
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()

    backtrack(0, [])

nums = [1, 2, 3]
generate_subsets(nums)
