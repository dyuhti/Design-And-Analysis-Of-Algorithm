def generate_subsets(nums, t):
    def backtrack(index, current_subset):
        current_sum = sum(current_subset)
        if current_sum == t:
            r.add(tuple(current_subset))
        elif current_sum > t:
            return

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()

    nums.sort()
    r = set()
    backtrack(0, [])
    for subset in r:
        print(list(subset))

nums = [10,1,2,7,6,1,5]
t = 8
generate_subsets(nums, t)
