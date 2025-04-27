MOD = 10 ** 9 + 7


def numberWays(hats):
    n = len(hats)
    num_hats = 0
    for h in hats:
        num_hats = max(num_hats, max(h))

    dp = [0] * (1 << (num_hats + 1))
    dp[0] = 1

    # Iterate through each person
    for i in range(n):
        for hat in hats[i]:
            # Iterate through each hat preferred by the person
            for mask in range(1 << (num_hats + 1)):
                # Check if the hat is not already assigned
                if mask & (1 << hat):
                    continue
                # Update dp[mask | (1 << hat)] by adding dp[mask]
                dp[mask | (1 << hat)] = (dp[mask | (1 << hat)] + dp[mask]) % MOD

    return dp[(1 << (num_hats + 1)) - 1]


# Example usage
print(numberWays([[3, 4], [4, 5], [5]]))  # Output: 1
print(numberWays([[3, 5, 1], [3, 5]]))  # Output: 4
