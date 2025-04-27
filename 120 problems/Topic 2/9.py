import math


def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def find_closest_pair(points):
    min_distance = float('inf')
    closest_pair = (None, None)

    n = len(points)

    for i in range(n):
        for j in range(i + 1, n):
            distance = calculate_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])

    return closest_pair, min_distance


# Example usage
points = [(1, 2), (4, 5), (7, 8), (3, 1)]
closest_pair, min_distance = find_closest_pair(points)
print(f"Closest pair: {closest_pair[0]} - {closest_pair[1]}")
print(f"Minimum distance: {min_distance}")
