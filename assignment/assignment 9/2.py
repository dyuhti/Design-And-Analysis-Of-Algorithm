import itertools

def check_constraints(permutation):
    a, b, c, d, e, f, g, h, i = permutation
    sum1 = a + b + c
    sum2 = c + d + e
    sum3 = e + f + g
    sum4 = g + h + i
    return sum1 == sum2 == sum3 == sum4

# Values to be used
values = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Find the valid permutation
for perm in itertools.permutations(values):
    if check_constraints(perm):
        print(f"Valid permutation: {perm}")
        break
else:
    print("No valid permutation found.")
