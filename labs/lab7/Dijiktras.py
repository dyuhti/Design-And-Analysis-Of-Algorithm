import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * (n)
    dist[ord(start) - 65] = 0
    pq = [(0, start)]
    previous_nodes = {node: None for node in graph}
    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[ord(node) - 65]:
            continue
        for neighbor, edge_cost in graph[node].items():
            if dist[ord(neighbor) - 65] > d + edge_cost:
                dist[ord(neighbor) - 65] = d + edge_cost
                heapq.heappush(pq, (dist[ord(neighbor) - 65], neighbor))
                previous_nodes[neighbor] = node
    return dist, previous_nodes

def reconstruct_path(previous_nodes, start, end):
    path = []
    while end is not None:
        path.append(end)
        end = previous_nodes[end]
    return path[::-1]

# Example usage:
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
shortest_distances, previous_nodes = dijkstra(graph, start_node)

# Print shortest distances and paths
for node in graph:
    path = reconstruct_path(previous_nodes, start_node, node)
    print(f"Shortest path to {node}: Distance = {shortest_distances[ord(node) - 65]}, Path = {' -> '.join(path)}")