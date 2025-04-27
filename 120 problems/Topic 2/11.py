import math


def orientation(p, q, r):
    """
    Determine the orientation of triplet (p, q, r).
    Returns:
     0 --> Collinear points
     1 --> Clockwise
    -1 --> Counterclockwise
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else -1


def calculate_center(points):
    """Calculate the center point of a set of points."""
    sum_x = sum(p[0] for p in points)
    sum_y = sum(p[1] for p in points)
    count = len(points)
    return (sum_x / count, sum_y / count)


def calculate_angle(point, center):
    """Calculate the angle of a point with respect to the center."""
    return math.atan2(point[1] - center[1], point[0] - center[0])


def convex_hull_brute_force(points):
    n = len(points)
    if n < 3:
        return points

    hull = set()

    for i in range(n):
        for j in range(n):
            if i != j:
                is_edge = True
                for k in range(n):
                    if k != i and k != j:
                        if orientation(points[i], points[j], points[k]) == -1:
                            is_edge = False
                            break
                if is_edge:
                    hull.add(points[i])
                    hull.add(points[j])

    # Convert hull to list and sort in counter-clockwise order
    hull = list(hull)
    center = calculate_center(hull)

    def sort_key(point):
        return calculate_angle(point, center)

    hull.sort(key=sort_key)

    return hull


# Test the implementation
points = [(1, 1), (4, 6), (8, 1), (0, 0), (3, 3)]
result = convex_hull_brute_force(points)
print("Convex Hull:", result)