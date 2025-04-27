import math
import matplotlib.pyplot as plt

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # collinear
    elif val > 0:
        return 1  # clockwise
    else:
        return 2  # counterclockwise

def polar_angle(base, p):
    return math.atan2(p[1] - base[1], p[0] - base[0])

def distance(base, p):
    return (p[0] - base[0]) ** 2 + (p[1] - base[1]) ** 2

def sort_points(base, points):
    def compare(p):
        angle = polar_angle(base, p)
        dist = distance(base, p)
        return (angle, dist)
    return sorted(points, key=compare)

def convex_hull(points):
    n = len(points)
    if n < 3:
        return points

    # Find the point with the lowest y-coordinate (and the leftmost one if there are ties)
    l = 0
    for i in range(1, n):
        if points[i][1] < points[l][1] or (points[i][1] == points[l][1] and points[i][0] < points[l][0]):
            l = i

    # Place the bottom-most point at the first position
    points[0], points[l] = points[l], points[0]

    # Sort the remaining points based on the angle with the base point
    base = points[0]
    sorted_points = sort_points(base, points[1:])

    hull = [points[0], sorted_points[0], sorted_points[1]]

    for i in range(2, n - 1):
        while len(hull) > 1 and orientation(hull[-2], hull[-1], sorted_points[i]) != 2:
            hull.pop()
        hull.append(sorted_points[i])

    return hull

# Example usage
points = [(0, 3), (2, 3), (1, 1), (2, 2), (4, 4), (0, 0), (1, 2), (3, 1), (3, 3)]
hull = convex_hull(points)

print("Convex Hull points:", hull)

# Plotting the points and the convex hull
x, y = zip(*points)
hx, hy = zip(*hull)
hx += (hx[0],)  # to create a closed path
hy += (hy[0],)  # to create a closed path

plt.scatter(x, y)
plt.plot(hx, hy, 'r-')
plt.show()
