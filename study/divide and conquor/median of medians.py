
def median_of_medians(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]

    # Divide arr into sublists of len 5
    sublists = [arr[i:i+5] for i in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]

    # Find the median of the medians
    pivot = median_of_medians(medians, len(medians) // 2)

    # Partitioning step
    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    pivot_count = len(arr) - len(low) - len(high)
    if k < len(low):
        return median_of_medians(low, k)
    elif k < len(low) + pivot_count:
        return pivot
    else:
        return median_of_medians(high, k - len(low) - pivot_count)

arr = [12, 3, 5, 7, 4, 19, 26, 14, 15, 6, 9, 8, 11, 13, 2]
k = len(arr) // 2 # For median
result = median_of_medians(arr, k)
print("Median of the array is:", result)
