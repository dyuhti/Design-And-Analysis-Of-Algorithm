def champagneTower(poured, query_row, query_glass):
    # Initialize the pyramid with all glasses having 0 champagne
    dp = [[0.0] * (i + 1) for i in range(101)]
    dp[0][0] = poured  # Pour the initial amount into the top glass

    for i in range(query_row + 1):
        next_dp = [[0.0] * (j + 1) for j in range(i + 1)]
        for j in range(len(dp[i])):
            if dp[i][j] >= 1:
                excess = dp[i][j] - 1
                next_dp[i][j] += 1  # Current glass gets fully filled with 1 cup
                if j < i:
                    next_dp[i][j + 1] += excess / 2  # Left glass gets half of the excess
                if j > 0:
                    next_dp[i][j - 1] += excess / 2  # Right glass gets half of the excess
        dp = next_dp

    return dp[query_row][query_glass]


# Examples
print(champagneTower(1, 1, 1))  # Output: 0.0
print(champagneTower(2, 1, 1))  # Output: 0.5
