def intToRoman(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    result = ""
    for i, v in enumerate(values):
        count = int(num / v)
        result += (numerals[i] * count)
        num -= v * count
    return result

# Example usage
print(intToRoman(3))     # Output: "III"
print(intToRoman(4))     # Output: "IV"
print(intToRoman(9))     # Output: "IX"
print(intToRoman(58))    # Output: "LVIII"
print(intToRoman(1994))  # Output: "MCMXCIV"