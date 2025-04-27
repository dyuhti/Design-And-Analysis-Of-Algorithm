import math

def calculate_distance(point1, point2):
    # Euclidean distance between two points
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def brute_force_closest_pair(points):
    n = len(points)
    min_distance = float('inf')
    closest_pair = None

    for i in range(n):
        for j in range(i + 1, n):
            distance = calculate_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])

    return closest_pair, min_distance

# Example usage:
points = [(1, 1), (4, 3), (5, 7), (10, 12), (2, 9)]
closest_pair, min_distance = brute_force_closest_pair(points)
print("Closest pair:", closest_pair)
print("Minimum distance:", min_distance)
