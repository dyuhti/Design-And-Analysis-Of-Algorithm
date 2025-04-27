class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False


def kruskal(graph):
    edges = []
    node_map = {}  # Map to convert node names to integer indices

    # Assign integer indices to nodes
    idx = 0
    for u in graph:
        node_map[u] = idx
        idx += 1

    # Create list of edges in format (weight, u, v)
    for u in graph:
        for v, weight in graph[u]:
            edges.append((weight, u, v))

    # Sort edges by weight
    edges.sort()

    n = len(graph)
    mst_cost = 0
    mst_edges = []
    uf = UnionFind(n)

    for weight, u, v in edges:
        u_idx = node_map[u]
        v_idx = node_map[v]

        if uf.union(u_idx, v_idx):
            mst_cost += weight
            mst_edges.append((u, v, weight))
            if len(mst_edges) == n - 1:
                break

    return mst_cost, mst_edges


# Example usage:
graph = {
    'A': [('B', 2), ('D', 4)],
    'B': [('A', 2), ('C', 1), ('D', 3)],
    'C': [('B', 1), ('D', 5)],
    'D': [('A', 4), ('B', 3), ('C', 5)]
}

mst_cost, mst_edges = kruskal(graph)

print("Minimum Spanning Tree Cost:", mst_cost)
print("Minimum Spanning Tree Edges:")
for u, v, weight in mst_edges:
    print(f"{u} -- {v} : {weight}")
