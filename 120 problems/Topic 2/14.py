def total_value(items, values):
    return sum(values[item] for item in items)

def is_feasible(items, weights, capacity):
    return sum(weights[item] for item in items) <= capacity


import itertools


def knapsack(weights, values, capacity):
    n = len(weights)
    max_value = 0
    best_selection = []

    for r in range(n + 1):
        for combination in itertools.combinations(range(n), r):
            if is_feasible(combination, weights, capacity):
                current_value = total_value(combination, values)
                if current_value > max_value:
                    max_value = current_value
                    best_selection = combination

    return max_value, best_selection

def print_test_case(weights, values, capacity):
    max_value, best_selection = knapsack(weights, values, capacity)
    print(f"Weights: {weights}")
    print(f"Values: {values}")
    print(f"Capacity: {capacity}")
    print(f"Optimal Selection: {list(best_selection)}")
    print(f"Total Value: {max_value}")
    print()

# Test Case 1
weights1 = [2, 3, 1]
values1 = [4, 5, 3]
capacity1 = 4
print_test_case(weights1, values1, capacity1)

# Test Case 2
weights2 = [1, 2, 3, 4]
values2 = [2, 4, 6, 3]
capacity2 = 6
print_test_case(weights2, values2, capacity2)
