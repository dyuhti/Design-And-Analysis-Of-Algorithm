MOD = 10 ** 9 + 7


def numberWays(hats):
    n = len(hats)
    max_hat = 40
    hat_to_people = [[] for _ in range(max_hat + 1)]

    for person, hat_list in enumerate(hats):
        for hat in hat_list:
            hat_to_people[hat].append(person)

    dp = [0] * (1 << n)
    dp[0] = 1

    for hat in range(1, max_hat + 1):
        for mask in range((1 << n) - 1, -1, -1):
            for person in hat_to_people[hat]:
                if mask & (1 << person) == 0:
                    dp[mask | (1 << person)] += dp[mask]
                    dp[mask | (1 << person)] %= MOD

    return dp[(1 << n) - 1]


# Example usage:
hats = [[3, 4], [4, 5], [5]]
print(numberWays(hats))  # Output: 1

hats = [[3, 5, 1], [3, 5]]
print(numberWays(hats))  # Output: 4

hats = [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]
print(numberWays(hats))  # Output: 24
