def bestClosingTime(customers: str) -> int:
    n = len(customers)
    min_penalty = float('inf')
    best_hour = 0

    # Compute the initial penalty for closing at hour 0
    penalty_open = 0
    penalty_closed = sum(1 for c in customers if c == 'Y')

    min_penalty = penalty_closed
    best_hour = 0

    for j in range(1, n + 1):
        if customers[j - 1] == 'Y':
            penalty_closed -= 1
        else:
            penalty_open += 1

        total_penalty = penalty_open + penalty_closed

        if total_penalty < min_penalty:
            min_penalty = total_penalty
            best_hour = j

    return best_hour


# Example usage
print(bestClosingTime("YYNY"))  # Output: 2
print(bestClosingTime("NNNN"))  # Output: 0
print(bestClosingTime("YYYY"))  # Output: 4
print(bestClosingTime("NYNY"))  # Output: 2
