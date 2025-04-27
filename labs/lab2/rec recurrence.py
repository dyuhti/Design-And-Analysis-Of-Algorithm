#master theorem
from math import log2


def master_theorem(a, b, f_n):
    if a < b**f_n(1):
        return "O(" + str(f_n(1)) + ")"
    elif a == b**f_n(1):
        return "O(" + str(f_n(1)) + " log n)"
    else:
        return "O(" + str(a) + "^n)"

# Example usage:
a = 2
b = 2
f_n = lambda n: n  # f(n) = n
print(master_theorem(a, b, f_n))  # Output: O(n log n)

#substitution methord
def substitution_method(T_n, guess):
    n = 1
    while True:
        if T_n(n) == guess(n):
            n *= 2
        else:
            break
    return "O(" + str(guess(1)) + ")"

# Example usage:
T_n = lambda n: 2*T_n(n/2) + n  # T(n) = 2T(n/2) + n
guess = lambda n: n*log2(n)  # Guess: T(n) = n log n
print(substitution_method(T_n, guess))  # Output: O(n log n)

#iteration methord
def iteration_method(T_n):
    n = 1
    iterations = 0
    while True:
        if T_n(n) == 1:  # Base case
            break
        n *= 2
        iterations += 1
    return "O(" + str(2**iterations) + ")"

# Example usage:
T_n = lambda n: 2*T_n(n/2) + n  # T(n) = 2T(n/2) + n
print(iteration_method(T_n))  # Output: O(n log n)
