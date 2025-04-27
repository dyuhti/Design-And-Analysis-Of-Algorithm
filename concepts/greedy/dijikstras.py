def dijkstra(graph, start):
    # Initialize the distances dictionary with infinity
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    # Track the shortest path
    shortest_path = {}
    # List to track nodes to visit
    nodes_to_visit = list(graph.keys())

    while nodes_to_visit:
        # Get the node with the smallest distance
        current_vertex = min(nodes_to_visit, key=lambda vertex: distances[vertex])
        nodes_to_visit.remove(current_vertex)

        # Skip if the smallest distance is infinity
        if distances[current_vertex] == float('inf'):
            break

        # Update the distance for each neighbor
        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path[neighbor] = current_vertex

    return distances, shortest_path

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
distances, shortest_path = dijkstra(graph, start_node)

print("Shortest distances from start node:")
for vertex in distances:
    print(f"{vertex}: {distances[vertex]}")

print("\nShortest path tree:")
for vertex in shortest_path:
    print(f"{vertex} <- {shortest_path[vertex]}")
