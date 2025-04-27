def median_of_medians(arr):
    # Base Case: Array size is small enough to find the median directly
    if len(arr) <= 5:
        return sorted(arr)[len(arr) // 2]

    # Divide the array into chunks of size 5
    chunks = [arr[i:i+5] for i in range(0, len(arr), 5)]

    # Find the median of each chunk
    medians = [sorted(chunk)[len(chunk) // 2] for chunk in chunks]

    # Recursively find the median of the medians
    pivot = median_of_medians(medians)

    # Partition the array based on the pivot
    lesser = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    # Determine the desired median's partition
    if len(lesser) == k:
        return pivot
    elif len(lesser) < k:
        return median_of_medians(greater)
    else:
        return median_of_medians(lesser)

# Example usage
arr = [5, 9, 2, 8, 3, 7, 1, 6, 4]
k = 5  # Index of the desired median (k-1)
result = median_of_medians(arr)
print(f"The median of {arr} is: {result}")