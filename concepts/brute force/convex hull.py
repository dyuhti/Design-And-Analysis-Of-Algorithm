def cross_product(o, a, b):
    # Returns the cross product of vector OA and OB
    # A positive cross product indicates a counter-clockwise turn, 0 indicates collinear, and negative indicates clockwise turn
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points):
    # Sort points lexicographically (tuples compare lexicographically in Python)
    points = sorted(points)

    # Build the lower hull
    lower_hull = []
    for p in points:
        while len(lower_hull) >= 2 and cross_product(lower_hull[-2], lower_hull[-1], p) <= 0:
            lower_hull.pop()
        lower_hull.append(p)

    # Build the upper hull
    upper_hull = []

    for p in reversed(points):
        while len(upper_hull) >= 2 and cross_product(upper_hull[-2], upper_hull[-1], p) <= 0:
            upper_hull.pop()
        upper_hull.append(p)

    # Remove last point of each half because it's repeated at the beginning of the other half
    return lower_hull[:-1] + upper_hull[:-1]

# Example usage:
points = [(0, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
hull = convex_hull(points)
print("Convex Hull points:", hull)
