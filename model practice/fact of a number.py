def factorial_recursive(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n - 1)

# Example usage:
number = 5
factorial_result = factorial_recursive(number)
print(f"The factorial of {number} is {factorial_result}.")
