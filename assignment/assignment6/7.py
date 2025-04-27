def find_pivot_integer(n: int) -> int:
    total_sum = n * (n + 1) // 2  # Total sum of integers from 1 to n

    left_sum = 0
    right_sum = total_sum

    for x in range(1, n + 1):
        right_sum -= x
        if left_sum == right_sum:
            return x
        left_sum += x

    return -1

# Example usage
print(find_pivot_integer(8))  # Output: 6