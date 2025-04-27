def uniquePaths(m, n):
    # Create a 2D dp array initialized with zeros
    dp = [[0] * n for _ in range(m)]

    # Base case: There is only 1 way to be at the starting point
    dp[0][0] = 1

    # Fill the dp array
    for i in range(m):
        for j in range(n):
            if i > 0:
                dp[i][j] += dp[i - 1][j]  # Add ways from above
            if j > 0:
                dp[i][j] += dp[i][j - 1]  # Add ways from the left

    # The result is the number of unique paths to reach bottom-right corner
    return dp[m - 1][n - 1]


# Examples
print(uniquePaths(7, 3))  # Output: 28
print(uniquePaths(3, 2))  # Output: 3
