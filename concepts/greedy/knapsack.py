def greedy_knapsack(values, weights, capacity):
    n = len(values)
    # Calculate value-to-weight ratios
    ratios = [(values[i] / weights[i], i) for i in range(n)]

    # Sort items by ratio in descending order
    ratios.sort(reverse=True)

    total_value = 0
    knapsack = [0] * n

    for ratio, index in ratios:
        if weights[index] <= capacity:
            knapsack[index] = 1
            total_value += values[index]
            capacity -= weights[index]
        else:
            break

    return total_value, knapsack


# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value, selected_items = greedy_knapsack(values, weights, capacity)
print(f"Maximum value: {max_value}")
print(f"Selected items: {selected_items}")