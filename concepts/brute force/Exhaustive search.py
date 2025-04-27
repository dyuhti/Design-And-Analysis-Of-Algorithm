import math


def function(x):
    # Define the function to minimize
    return x ** 2 - 4 * x + 5


def exhaustive_search_minimization(func, range_start, range_end, step_size=0.1):
    # Initialize variables to track minimum value and corresponding x
    min_value = math.inf
    min_x = None

    # Iterate through the range with the specified step size
    x = range_start
    while x <= range_end:
        # Calculate function value at current x
        fx = func(x)

        # Update minimum value and corresponding x if a new minimum is found
        if fx < min_value:
            min_value = fx
            min_x = x

        # Move to the next x value
        x += step_size

    return min_value, min_x

# Example usage:
range_start = -10
range_end = 10
step_size = 0.1

min_value, min_x = exhaustive_search_minimization(function, range_start, range_end, step_size)
print(f"Minimum value found: {min_value} at x = {min_x}")
