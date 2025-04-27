def canBreak(s1, s2):
    # Sort the strings
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)

    # Check if s1 can break s2
    can_break_s1 = all(s1_sorted[i] >= s2_sorted[i] for i in range(len(s1)))

    # Check if s2 can break s1
    can_break_s2 = all(s2_sorted[i] >= s1_sorted[i] for i in range(len(s1)))

    return can_break_s1 or can_break_s2

# Example usage
print(canBreak("abc", "xya"))  # Output: True
print(canBreak("abe", "acd"))  # Output: False
