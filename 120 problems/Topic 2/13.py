def total_cost(assignment, cost_matrix):
    cost = 0
    for worker, task in enumerate(assignment):
        cost += cost_matrix[worker][task]
    return cost


import itertools


def assignment_problem(cost_matrix):
    n = len(cost_matrix)
    workers = range(n)

    min_cost = float('inf')
    best_assignment = []

    for assignment in itertools.permutations(workers):
        current_cost = total_cost(assignment, cost_matrix)

        if current_cost < min_cost:
            min_cost = current_cost
            best_assignment = assignment

    return min_cost, best_assignment

def print_test_case(cost_matrix):
    min_cost, best_assignment = assignment_problem(cost_matrix)
    print(f"Cost Matrix: {cost_matrix}")
    print(f"Best Assignment: {best_assignment}")
    print(f"Minimum Cost: {min_cost}")
    print()

# Test Case 1
cost_matrix1 = [
    [9, 2, 7, 8],
    [6, 4, 3, 7],
    [5, 8, 1, 8],
    [7, 6, 9, 4]
]
print_test_case(cost_matrix1)

# Test Case 2
cost_matrix2 = [
    [4, 1, 3],
    [2, 0, 5],
    [3, 2, 2]
]
print_test_case(cost_matrix2)

# Test Case 3
cost_matrix3 = [
    [11, 12, 18],
    [6, 7, 8],
    [12, 15, 11]
]
print_test_case(cost_matrix3)
