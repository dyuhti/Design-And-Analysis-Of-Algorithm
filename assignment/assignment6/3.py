def minCutsToDivideCircle(n: int) -> int:
    if n == 1:
        return 0
    elif n % 2 == 0:
        return n // 2
    else:
        return n

# Example usage
print(minCutsToDivideCircle(4))  # Output: 2
print(minCutsToDivideCircle(3))  # Output: 3
print(minCutsToDivideCircle(1))  # Output: 0
