def prime_factors(n, factor=2):
    if n <= 1:
        return []
    elif n % factor == 0:
        return [factor] + prime_factors(n // factor, factor)
    else:
        return prime_factors(n, factor + 1)


def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


def gcd(a, b):
    factors_a = prime_factors(a)
    factors_b = prime_factors(b)

    common_factors = set(factors_a) & set(factors_b)

    result = 1
    for factor in common_factors:
        result *= factor

    return result


num1 = 48
num2 = 60
print("GCD of", num1, "and", num2, "is:", gcd(num1, num2))  # Output: 12
