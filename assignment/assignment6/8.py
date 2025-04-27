def minAppendedChars(s: str, t: str) -> int:
    m, n = len(s), len(t)
    i, j = 0, 0
    longest_common_subsequence = 0

    while i < m and j < n:
        if s[i] == t[j]:
            longest_common_subsequence += 1
            i += 1
            j += 1
        else:
            i += 1

    return n - longest_common_subsequence
print(minAppendedChars("coaching", "coding"))  # Output: 4
print(minAppendedChars("abcde", "ace"))  # Output: 0
print(minAppendedChars("abc", "def"))  # Output: 3