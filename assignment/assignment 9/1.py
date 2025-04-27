import heapq


def prim(graph, start_node):
    # Initialize the minimum spanning tree (MST) and visited set
    mst = []
    visited = set([start_node])

    # Initialize the priority queue with the edges of the start node
    edges = [(cost, start_node, to) for to, cost in graph[start_node].items()]
    heapq.heapify(edges)

    # Loop until the priority queue is empty
    while edges:
        cost, frm, to = heapq.heappop(edges)

        # If the to node is already visited, continue
        if to in visited:
            continue

        # Add the edge to the MST
        mst.append((frm, to, cost))
        visited.add(to)

        # Add the edges of the newly visited node to the priority queue
        for to_next, cost_next in graph[to].items():
            if to_next not in visited:
                heapq.heappush(edges, (cost_next, to, to_next))

    return mst


# Define the graph as an adjacency list
graph = {
    'a': {'c': 5, 'b': 2},
    'b': {'a': 3, 'c': 1, 'd': 1},
    'c': {'a': 5, 'b': 1},
    'd': {'b': 1}
}

# Starting node
start_node = 'a'

# Find the minimum spanning tree using Prim's algorithm
mst = prim(graph, start_node)
print("Minimum Spanning Tree:", mst)
