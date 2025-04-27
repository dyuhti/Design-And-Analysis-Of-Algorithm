import heapq


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1


def prims_algorithm(graph, start_vertex):
    mst = []
    visited = set()
    min_heap = [(0, start_vertex, None)]  # (weight, vertex, parent)
    total_cost = 0
    while min_heap:
        weight, u, parent = heapq.heappop(min_heap)
        if u not in visited:
            visited.add(u)
            if parent is not None:
                mst.append((parent, u, weight))
                total_cost += weight
            for v, w in graph[u]:
                if v not in visited:
                    heapq.heappush(min_heap, (w, v, u))
    return mst, total_cost


def kruskals_algorithm(graph, num_vertices):
    edges = []
    for u in graph:
        for v, w in graph[u]:
            edges.append((w, u, v))
    edges.sort()
    uf = UnionFind(num_vertices)
    mst = []
    total_cost = 0
    for weight, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
            total_cost += weight
    return mst, total_cost


def boruvkas_algorithm(graph, num_vertices):
    uf = UnionFind(num_vertices)
    mst = []
    total_cost = 0
    num_components = num_vertices
    while num_components > 1:
        cheapest = [-1] * num_vertices
        for u in graph:
            for v, w in graph[u]:
                u_root = uf.find(u)
                v_root = uf.find(v)
                if u_root != v_root:
                    if cheapest[u_root] == -1 or cheapest[u_root][0] > w:
                        cheapest[u_root] = (w, u, v)
                    if cheapest[v_root] == -1 or cheapest[v_root][0] > w:
                        cheapest[v_root] = (w, v, u)
        for u in range(num_vertices):
            if cheapest[u] != -1:
                w, u, v = cheapest[u]
                if uf.find(u) != uf.find(v):
                    uf.union(u, v)
                    mst.append((u, v, w))
                    total_cost += w
                    num_components -= 1
    return mst, total_cost


graph = {
    0: [(1, 10), (2, 6), (3, 5)],
    1: [(0, 10), (3, 15)],
    2: [(0, 6), (3, 4)],
    3: [(0, 5), (1, 15), (2, 4)]
}
num_vertices = len(graph)
mst_prims, cost_prims = prims_algorithm(graph, 0)
print("Prim's Algorithm MST:", mst_prims)
print("Prim's Algorithm Cost:", cost_prims)
mst_kruskals, cost_kruskals = kruskals_algorithm(graph, num_vertices)
print("Kruskal's Algorithm MST:", mst_kruskals)
print("Kruskal's Algorithm Cost:", cost_kruskals)
mst_boruvkas, cost_boruvkas = boruvkas_algorithm(graph, num_vertices)
print("Boruvka's Algorithm MST:", mst_boruvkas)
print("Boruvka's Algorithm Cost:", cost_boruvkas)
