def prim_mst(graph):
    # Initialize the MST and set of visited vertices
    mst = []
    visited = set()

    # Start with an arbitrary vertex (e.g., the first one in the graph)
    start_vertex = next(iter(graph))
    visited.add(start_vertex)

    while len(visited) < len(graph):
        min_edge = None
        for vertex in visited:
            for neighbor, weight in graph[vertex].items():
                if neighbor not in visited:
                    if min_edge is None or weight < min_edge[2]:
                        min_edge = (vertex, neighbor, weight)

        if min_edge is not None:
            mst.append(min_edge)
            visited.add(min_edge[1])

    return mst


# Example usage
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
    'E': {'C': 10, 'D': 2, 'F': 3},
    'F': {'D': 6, 'E': 3}
}

minimum_spanning_tree = prim_mst(graph)

print("Edges in the Minimum Spanning Tree:")
for edge in minimum_spanning_tree:
    print(f"{edge[0]} -- {edge[1]} : {edge[2]}")