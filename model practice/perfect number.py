def is_perfect_number(number):
    if number <= 0:
        return False

    Sum = 0
    for i in range(1, number):
        if number % i == 0:
            Sum += i

    if Sum == number:
        return True
    else:
        return False


# Example usage:
Input_Number = 28

if is_perfect_number(Input_Number):
    print(f"{Input_Number} is a Perfect Number.")
else:
    print(f"{Input_Number} is not a Perfect Number.")
