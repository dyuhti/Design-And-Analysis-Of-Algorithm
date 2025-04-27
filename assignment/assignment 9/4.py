def subset_sum(S, d):
    def backtrack(start, current_subset, current_sum):
        if current_sum == d:
            result.append(current_subset[:])
            return
        if current_sum > d:
            return

        for i in range(start, len(S)):
            current_subset.append(S[i])
            backtrack(i + 1, current_subset, current_sum + S[i])
            current_subset.pop()

    result = []
    S.sort()  # Sorting is not necessary but can help with optimizations
    backtrack(0, [], 0)
    return result


# Given set and target sum
S = [5, 10, 12, 13, 15, 18]
d = 30

# Find all subsets that sum up to d
subsets = subset_sum(S, d)
print("Subsets that sum to", d, ":", subsets)
