def assembly_line_scheduling(a, t, e, x):
    num_lines = len(a)
    num_stations = len(a[0])

    # Initialize f: f[i][j] is the minimum time to get to station j on line i
    f = [[0 for _ in range(num_stations)] for _ in range(num_lines)]

    # Initialize first station for each line
    for i in range(num_lines):
        f[i][0] = e[i] + a[i][0]

    # Fill the f table
    for j in range(1, num_stations):
        for i in range(num_lines):
            # Time to stay on the same line
            same_line = f[i][j - 1] + a[i][j]

            # Time to switch from other lines
            other_lines = [f[k][j - 1] + t[k][i] + a[i][j] for k in range(num_lines) if k != i]

            # Choose the minimum time
            f[i][j] = min(same_line, min(other_lines))

    # Find the minimum time to exit from the last station of any line
    return min(f[i][-1] + x[i] for i in range(num_lines))


# Example usage
a = [
    [4, 5, 3, 2],
    [2, 10, 1, 4],
    [3, 6, 8, 5]
]
t = [
    [0, 7, 4, 5],
    [0, 9, 2, 8],
    [0, 3, 6, 4]
]
e = [10, 12, 8]#entry time for each line
x = [18, 7, 10]#exit time for each line

fastest_time = assembly_line_scheduling(a, t, e, x)
print(f"The fastest production time is {fastest_time}")