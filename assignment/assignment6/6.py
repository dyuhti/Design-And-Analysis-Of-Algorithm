def count_palindromic_subsequences(s):
    n = len(s)
    count = 0

    def is_palindrome(start, end):
        if start >= end:
            return True
        if s[start] != s[end]:
            return False
        return is_palindrome(start + 1, end - 1)

    for i in range(n - 4):
        for j in range(i + 5, n + 1):  # Corrected range
            if is_palindrome(i, j - 1):
                count += 1

    return count

s = input()
print(count_palindromic_subsequences(s))
