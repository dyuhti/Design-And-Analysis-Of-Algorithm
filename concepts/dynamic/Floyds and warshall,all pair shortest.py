INF = float('inf')

def floyd_warshall(graph):
    """
    Floyd-Warshall algorithm to find shortest paths between all pairs of vertices.
    :param graph: 2D list representing the adjacency matrix of the graph.
    :return: A 2D list dist where dist[i][j] is the shortest distance from vertex i to vertex j.
    """
    V = len(graph)
    dist = [row[:] for row in graph]  # Copy the graph to not modify the original

    # Compute shortest paths
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Example usage:
graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

shortest_paths = floyd_warshall(graph)
for row in shortest_paths:
    print(row)
