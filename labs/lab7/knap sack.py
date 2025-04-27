def fractional_knapsack(weights, values, capacity):
    n = len(values)
    items = sorted([(values[i]/weights[i], weights[i], values[i]) for i in range(n)], reverse=True)

    total_value = 0
    for item in items:
        if capacity >= item[1]:
            capacity -= item[1]
            total_value += item[2]
        else:
            total_value += item[0] * capacity
            break

    return total_value

# Example usage:
weights = [1, 2, 4, 2, 5]
values = [5, 3, 5, 3, 2]
capacity = 10

max_value = fractional_knapsack(weights, values, capacity)
print(f"Maximum value that can be put in a knapsack of capacity {capacity}: {max_value}")