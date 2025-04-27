def optimal_bst(keys, freq):
    n = len(keys)
    # Create a 2D array to store minimum cost of searching keys[i..j]
    cost = [[0] * n for _ in range(n)]

    # Base case: Single keys have the same cost as their frequencies
    for i in range(n):
        cost[i][i] = freq[i]

    # Build the dp table for different chain lengths
    for length in range(2, n + 1):  # length of subtree
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float('inf')
            sum_freq = sum(freq[i:j+1])

            for k in range(i, j + 1):
                left_cost = cost[i][k - 1] if k > i else 0
                right_cost = cost[k + 1][j] if k < j else 0
                total = left_cost + right_cost + sum_freq
                if total < cost[i][j]:
                    cost[i][j] = total

    return cost[0][n - 1]

# Example usage:
keys = [10, 12, 20]
freq = [34, 8, 50]

min_cost = optimal_bst(keys, freq)
print(f"Minimum cost of optimal BST: {min_cost}")
