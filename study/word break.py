def word_break(s, dict):
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in dict:
                dp[i] = True
                break

    return dp[-1]

s = "pineapplepenapple"
dict = {"apple", "pen", "applepen", "pine", "pineapple"}

result = word_break(s, dict)
print("Can be segmented:",result)