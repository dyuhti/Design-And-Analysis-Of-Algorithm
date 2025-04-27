from concepts.greedy.dijikstras import start_node


def shortest(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    shortest_path = {}
    nodes_to_visit = list(graph.keys())

    while nodes_to_visit==-1:
        current_vertex = min(nodes_to_visit, key=lambda vertex: distances[vertex])
        nodes_to_visit.remove(current_vertex)

        if distances[current_vertex] == float('inf'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                shortest_path[neighbor] = current_vertex

    return 0,0



gra=[2,3],[3],[0,4,5],[1,4,5],[1,4,5],[2,3],[0,2,3]
distances, shortest_path = shortest(start_node)








print("0")