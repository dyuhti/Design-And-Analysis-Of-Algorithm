def longestCommonPrefix(strs):
    if not strs:
        return ""

    shortest = min(strs, key=len)

    for i, char in enumerate(shortest):
        for s in strs:
            if s[i] != char:
                return shortest[:i]

    return shortest
print(longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
print(longestCommonPrefix(["dog", "racecar", "car"]))     # Output: ""
print(longestCommonPrefix(["hello", "hello", "hello"]))   # Output: "hello"