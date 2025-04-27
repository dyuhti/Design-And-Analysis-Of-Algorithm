def greedy_coloring(graph):
    # Initialize the result dictionary
    result = {}

    # Assign the first color to the first vertex
    for vertex in graph:
        # Find the colors of the adjacent vertices
        adjacent_colors = set(result.get(neighbor) for neighbor in graph[vertex])

        # Find the first color that is not used by the adjacent vertices
        color = 1
        while color in adjacent_colors:
            color += 1

        # Assign the found color to the current vertex
        result[vertex] = color

    return result


# Define the graph
graph = {
    'a': ['b', 'c', 'e'],
    'b': ['a', 'c', 'd'],
    'c': ['a', 'b', 'd', 'e'],
    'd': ['b', 'c', 'e', 'f'],
    'e': ['a', 'c', 'd', 'f'],
    'f': ['d', 'e']
}

# Apply the greedy coloring algorithm
coloring = greedy_coloring(graph)

# Print the coloring result
print("Vertex colors:", coloring)

# Find the chromatic number
chromatic_number = max(coloring.values())
print("Chromatic number:", chromatic_number)
