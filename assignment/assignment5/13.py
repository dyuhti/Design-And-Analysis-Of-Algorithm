def max_chunks_to_sorted(arr):
    max_val = 0
    chunks = 0

    for i, num in enumerate(arr):
        max_val = max(max_val, num)

        if i == max_val:
            chunks += 1

    return chunks


# Example usage
arr1 = [4, 3, 2, 1, 0]
arr2 = [1, 0, 2, 3, 4]

print("Example 1 Output:", max_chunks_to_sorted(arr1))  # Output: 1
print("Example 2 Output:", max_chunks_to_sorted(arr2))  # Output: 4
