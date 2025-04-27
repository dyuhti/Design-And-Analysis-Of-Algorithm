def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

def is_armstrong(n, digit_count):
    if n == 0:
        return 0
    return (n % 10) ** digit_count + is_armstrong(n // 10, digit_count)

def check_armstrong(n):
    digit_count = count_digits(n)
    sum_of_powers = is_armstrong(n, digit_count)
    return sum_of_powers == n

# Example usage:
num = 153
if check_armstrong(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
