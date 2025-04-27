def generate_subsets(nums,t):
    def backtrack(index, current_subset):

        if sum(current_subset) ==t:
            print(current_subset)

        for i in range(index, len(nums)):
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()

    backtrack(0, [])

nums = [10,1,2,7,6,1,5]
t=8
generate_subsets(nums)
