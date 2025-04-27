def max_min(arr, low, high):
    if low == high:
        return (arr[low], arr[low])
    elif high == low + 1:
        if arr[low] < arr[high]:
            return (arr[low], arr[high])
        else:
            return (arr[high], arr[low])
    else:
        mid = (low + high) // 2
        (leftMin, leftMax) = max_min(arr, low, mid)
        (rightMin, rightMax) = max_min(arr, mid + 1, high)
        Omin = min(leftMin, rightMin)
        Omax = max(leftMax, rightMax)
        return (Omin, Omax)


def min(a, b):
    if a < b:
        return a
    else:
        return b


def max(a, b):
    if a > b:
        return a
    else:
        return b


# Example usage:
arr = [7, 3, 4, 5, 6, 4, 2, 1]
low = 0
high = len(arr) - 1
result = max_min(arr, low, high)
print(f"Minimum element is {result[0]} and Maximum element is {result[1]}")
