def max_sum_subsequence_no_adjacent(nums):
    incl = 0
    excl = 0

    for num in nums:
        new_excl = max(incl, excl)
        incl = excl + num
        excl = new_excl

    return max(incl, excl)


def sum_of_queries_results(nums, queries):
    MOD = 10 ** 9 + 7
    total_sum = 0

    for pos, val in queries:
        nums[pos] = val
        max_sum = max_sum_subsequence_no_adjacent(nums)
        total_sum = (total_sum + max_sum) % MOD

    return total_sum


# Example usage
nums = [1, 2, 3]
queries = [[1, 5], [0, 4]]
print(sum_of_queries_results(nums, queries))  # Output should be the sum of results for each query

