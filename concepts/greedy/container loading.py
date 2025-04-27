def bin_packing(weights, bin_capacity):
    # Sort the weights in descending order
    weights.sort(reverse=True)

    # Initialize a list to hold the bins
    bins = []

    # Iterate over each weight
    for weight in weights:
        # Try to place the weight in an existing bin
        placed = False
        for b in bins:
            if sum(b) + weight <= bin_capacity:
                b.append(weight)
                placed = True
                break
        # If the weight cannot be placed in any existing bin, create a new bin
        if not placed:
            bins.append([weight])

    return bins


# Example usage
weights = [4, 8, 1, 4, 2, 1]
bin_capacity = 10

result = bin_packing(weights, bin_capacity)
print(f"Number of bins required: {len(result)}")
for i, b in enumerate(result):
    print(f"Bin {i + 1}: {b}")
