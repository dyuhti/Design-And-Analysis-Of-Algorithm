def destCity(paths):
    outgoing = set()

    # Collect all cities with outgoing paths
    for path in paths:
        outgoing.add(path[0])

    # The destination city will be a city with no outgoing paths
    for path in paths:
        if path[1] not in outgoing:
            return path[1]


# Example usage:
paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
print(destCity(paths))  # Output: "Sao Paulo"

paths = [["B", "C"], ["D", "B"], ["C", "A"]]
print(destCity(paths))  # Output: "A"

paths = [["A", "Z"]]
print(destCity(paths))  # Output: "Z"
