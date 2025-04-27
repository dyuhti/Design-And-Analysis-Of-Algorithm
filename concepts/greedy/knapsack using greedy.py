def knapsack_fractional(weights, values, capacity):
    # Create a list of tuples (value, weight, index)
    items = [(values[i] / weights[i], weights[i], values[i]) for i in range(len(weights))]

    # Sort items by value-to-weight ratio in descending order
    items.sort(reverse=True, key=lambda x: x[0])

    total_value = 0.0
    remaining_capacity = capacity

    for ratio, weight, value in items:
        if remaining_capacity <= 0:
            break
        if weight <= remaining_capacity:
            total_value += value
            remaining_capacity -= weight
        else:
            total_value += ratio * remaining_capacity
            remaining_capacity = 0

    return total_value


# Example usage:
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

max_value = knapsack_fractional(weights, values, capacity)
print(f"The maximum value that can be obtained is: {max_value}")
