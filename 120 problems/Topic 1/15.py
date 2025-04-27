def largeGroupPositions(s):
    result = []
    n = len(s)
    start = 0

    for i in range(1, n):
        if s[i] != s[i - 1]:
            if i - start >= 3:
                result.append([start, i - 1])
            start = i

    # Check the last group
    if n - start >= 3:
        result.append([start, n - 1])

    return result


# Examples
print(largeGroupPositions("abbxxxxzzy"))  # Output: [[3, 6]]
print(largeGroupPositions("abc"))  # Output: []
