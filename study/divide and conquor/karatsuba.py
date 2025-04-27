def karatsuuba(x, y):
    if x < 10 or y < 10:
        return x * y

    # Calculates the size
    n = max(len(str(x)), len(str(y)))
    half = n // 2

    # splits the nos into 2 halves
    high1, low1 = divmod(x, 10 ** half)
    high2, low2 = divmod(y, 10 ** half)

    z0 = karatsuuba(low1, low2)
    z1 = karatsuuba((low1 + high1), (low2 + high2))
    z2 = karatsuuba(high1, high2)

    return (z2 * 10 ** (2 * half)) + ((z1 - z2 - z0) * 10 ** half) + z0


x = 12345678
y = 87654321
result = karatsuuba(x, y)
print(result)
