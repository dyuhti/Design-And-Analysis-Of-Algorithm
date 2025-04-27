import math

def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)


import itertools


def tsp(cities):
    n = len(cities)
    if n == 0:
        return 0, []

    min_distance = float('inf')
    shortest_path = []
    start_city = cities[0]
    remaining_cities = cities[1:]

    for perm in itertools.permutations(remaining_cities):
        current_path = [start_city] + list(perm) + [start_city]
        current_distance = 0

        for i in range(len(current_path) - 1):
            current_distance += distance(current_path[i], current_path[i + 1])

        if current_distance < min_distance:
            min_distance = current_distance
            shortest_path = current_path

    return min_distance, shortest_path

def print_test_case(cities):
    min_distance, shortest_path = tsp(cities)
    print(f"Cities: {cities}")
    print(f"Shortest path: {shortest_path}")
    print(f"Minimum distance: {min_distance}")
    print()

# Test Case 1
cities1 = [(0, 0), (1, 1), (2, 2), (3, 3)]
print_test_case(cities1)

# Test Case 2
cities2 = [(0, 0), (2, 0), (2, 2), (0, 2)]
print_test_case(cities2)

# Test Case 3
cities3 = [(0, 0), (1, 0), (1, 1), (0, 1)]
print_test_case(cities3)
