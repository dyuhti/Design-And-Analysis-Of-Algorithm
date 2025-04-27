def prim_mst(graph):
    # Choose an arbitrary starting vertex
    start_vertex = next(iter(graph))
    mst = []
    visited = set([start_vertex])
    vertices = set(graph.keys())

    while len(visited) < len(vertices):
        min_edge = None
        for v in visited:
            for neighbor, weight in graph[v].items():
                if neighbor not in visited:
                    if min_edge is None or weight < min_edge[2]:
                        min_edge = (v, neighbor, weight)

        if min_edge is not None:
            frm, to, cost = min_edge
            visited.add(to)
            mst.append((frm, to, cost))

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