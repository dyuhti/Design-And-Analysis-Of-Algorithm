def checkIfCanBreak(s1: str, s2: str) -> bool:
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)

    return (all(x >= y for x, y in zip(s1_sorted, s2_sorted)) or
            all(x >= y for x, y in zip(s2_sorted, s1_sorted)))


# Example usage:
s1 = "abc"
s2 = "xya"
print(checkIfCanBreak(s1, s2))  # Output: True