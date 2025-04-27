def is_armstrong(num):
    # Calculate the number of digits
    num_str = str(num)
    num_digits = len(num_str)

    # Calculate the sum of each digit raised to the power of num_digits
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_digits

    # Check if the number is Armstrong
    if sum == num:
        return True
    else:
        return False


# Example usage:
num = 153
if is_armstrong(num):
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")
