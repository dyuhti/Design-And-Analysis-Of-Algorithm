import heapq

def min_cost_to_buy_apples(n, roads, appleCost, k):
    graph = [[] for _ in range(n + 1)]
    for a, b, cost in roads:
        graph[a].append((b, cost))
        graph[b].append((a, cost))

        #graph = [
#     [],                 # City 0 (unused)
#     [(2, 4), (3, 4)],   # City 1 has roads to City 2 (cost 4) and City 3 (cost 4)
#     [(1, 4), (3, 2), (4, 5)],  # City 2 has roads to City 1 (cost 4), City 3 (cost 2), and City 4 (cost 5)
#     [(2, 2), (4, 1), (1, 4)],  # City 3 has roads to City 2 (cost 2), City 4 (cost 1), and City 1 (cost 4)
#     [(2, 5), (3, 1)]    # City 4 has roads to City 2 (cost 5) and City 3 (cost 1)
# ]


    def dijkstra(start):
        dist = [float('inf')] * (n + 1)
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            for neighbor, edge_cost in graph[node]:
                if dist[neighbor] > d + edge_cost:
                    dist[neighbor] = d + edge_cost
                    heapq.heappush(pq, (dist[neighbor], neighbor))
        return dist

    res = []
    for i in range(1, n + 1):
        dist = dijkstra(i)
        min_cost = appleCost[i - 1]  # handle the case where the apple is bought at the starting city
        for j in range(1, n + 1):
            if i!= j:
                min_cost = min(min_cost, dist[j] + appleCost[j - 1] + k * dist[j])
        res.append(min_cost)

    return res

n = 4
roads = [[1,2,4],[2,3,2],[2,4,5],[3,4,1],[1,3,4]]
appleCost = [56,42,102,301]
k = 2
print(min_cost_to_buy_apples(n, roads, appleCost, k))  # Output: [54, 42, 48, 51]