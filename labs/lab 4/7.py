def maximumGap(num: int) -> int:
    num_str = str(num)
    max_num = int(''.join('9' if c != '0' else c for c in num_str))
    min_num = int(''.join('1' if c == '9' else '0' if c == '0' else '1' for c in num_str))
    return max_num - min_num

# Example usage:
num = 555
print(maximumGap(num))  # Output: 888