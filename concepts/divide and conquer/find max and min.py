def max_dc(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        mid = len(arr) // 2
        left_max = max_dc(arr[:mid])
        right_max = max_dc(arr[mid:])
        return max(left_max, right_max)

def min_dc(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        mid = len(arr) // 2
        left_min = min_dc(arr[:mid])
        right_min = min_dc(arr[mid:])
        return min(left_min, right_min)

# Example usage:
arr = [3, 1, 4, 1, 5, 9, 2, 6]
print("Maximum element:", max_dc(arr))
print("Minimum element:", min_dc(arr))