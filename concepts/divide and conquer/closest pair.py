import math


def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def brute_force_closest_pair(points):
    """Find the closest pair of points using brute-force method."""
    n = len(points)
    if n < 2:
        return float('inf'), None, None

    min_distance = float('inf')
    closest_pair = None

    for i in range(n):
        for j in range(i + 1, n):
            distance = euclidean_distance(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])

    return min_distance, closest_pair


# Example usage:
points = [(1, 1), (2, 5), (0, 0), (4, 3), (3, 2)]
min_dist, closest_pair = brute_force_closest_pair(points)
print(f"Closest pair: {closest_pair} with distance {min_dist}")
