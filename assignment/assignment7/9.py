from collections import deque


def minFuel(roads, seats):
    n = len(roads) + 1  # Number of cities
    if n == 1:
        return 0  # Only one city, already at the capital

    # Create adjacency list representation of the graph
    graph = [[] for _ in range(n)]
    for road in roads:
        a, b = road
        graph[a].append(b)
        graph[b].append(a)

    # BFS setup
    queue = deque([0])  # Start from city 0 (capital)
    visited = [False] * n
    visited[0] = True
    fuel_cost = 0

    while queue:
        size = len(queue)
        for _ in range(size):
            current = queue.popleft()
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
                    fuel_cost += 1  # Each level of BFS represents 1 liter of fuel

        # Check if all cities are visited
        if all(visited):
            break

    return fuel_cost


# Example usage:
roads = [[0, 1], [0, 2], [0, 3]]
seats = 5
print(minFuel(roads, seats))  # Output: 3
