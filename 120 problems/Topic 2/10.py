import math


def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def closest_pair_brute_force(points):
    n = len(points)
    if n < 2:
        return None

    min_distance = float('inf')
    closest_pair = None

    for i in range(n):
        for j in range(i + 1, n):
            distance = euclidean_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])

    return closest_pair, min_distance


# Test the implementation
points = [(10, 0), (11, 5), (5, 3), (9, 3.5), (15, 3), (12.5, 7), (6, 6.5), (7.5, 4.5)]
result, distance = closest_pair_brute_force(points)
print(f"Closest pair: {result}")
print(f"Distance: {distance}")