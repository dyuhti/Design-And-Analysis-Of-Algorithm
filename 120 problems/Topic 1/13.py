def climbStairs(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2

    dp = [0] * (n + 1)
    dp[0] = 1  # 1 way to climb 0 steps (doing nothing)
    dp[1] = 1  # 1 way to climb 1 step
    dp[2] = 2  # 2 ways to climb 2 steps (1+1 or 2)

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# Examples
print(climbStairs(4))  # Output: 5
print(climbStairs(3))  # Output: 3
