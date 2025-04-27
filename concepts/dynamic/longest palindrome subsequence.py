def longest_palindromic_subsequence(s):
    n = len(s)
    # Create a 2D array to store lengths of longest palindromic subsequence
    dp = [[0] * n for _ in range(n)]

    # All substrings of length 1 are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Build the dp table
    for length in range(2, n + 1):  # length of substring
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and length == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]

# Example usage:
s = "bbbab"
print("Longest palindromic subsequence length:", longest_palindromic_subsequence(s))  # Output: 4
