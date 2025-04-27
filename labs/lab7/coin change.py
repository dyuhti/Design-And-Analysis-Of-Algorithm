def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# Example usage:
coins = [2,6,4]
amount = 12
min_coins = coin_change(coins, amount)

print(f"Minimum coins needed to make {amount}: {min_coins}")