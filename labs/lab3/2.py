def checkIfCanBreak(s1, s2):
    # Step 1: Count frequency of characters
    count_s1 = [0] * 26
    count_s2 = [0] * 26

    for char in s1:
        count_s1[ord(char) - ord('a')] += 1

    for char in s2:
        count_s2[ord(char) - ord('a')] += 1

    # Step 2: Calculate cumulative sums
    sum_s1 = sum_s2 = 0
    for i in range(26):
        sum_s1 += count_s1[i]
        sum_s2 += count_s2[i]

        # Step 3: Compare cumulative sums
        if sum_s1 < sum_s2:
            return False

    return True


# Example usage
s1 = "abc"
s2 = "xya"
print(checkIfCanBreak(s1, s2))  # Output: True

s1 = "abe"
s2 = "acd"
print(checkIfCanBreak(s1, s2))  # Output: False
