def dice_throw(n, m, S):
    # dp[i][j] will store the number of ways to get sum j using i dice
    dp = [[0] * (S + 1) for _ in range(n + 1)]

    # Initialize base cases
    dp[0][0] = 1  # 1 way to get sum 0 with 0 dice (by not throwing any dice)

    # Build dp table
    for i in range(1, n + 1):
        for j in range(1, S + 1):
            for k in range(1, min(m, j) + 1):
                dp[i][j] += dp[i - 1][j - k]

    return dp[n][S]

# Example usage:
n = 3  # Number of dice
m = 6  # Number of faces on each die (1 through 6)
S = 8  # Desired sum

ways = dice_throw(n, m, S)
print(f"Number of ways to get sum {S} with {n} dice: {ways}")
