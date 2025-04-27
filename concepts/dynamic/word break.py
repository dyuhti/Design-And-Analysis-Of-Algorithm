def word_break(s, word_dict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string is always breakable

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break

    return dp[n]

# Example usage:
word_dict = {"apple", "pen", "applepen", "pine", "pineapple"}
s1 = "applepenapple"  # Output: True
s2 = "catsandog"      # Output: False

print(f"Can '{s1}' be segmented into dictionary words? {word_break(s1, word_dict)}")
print(f"Can '{s2}' be segmented into dictionary words? {word_break(s2, word_dict)}")
