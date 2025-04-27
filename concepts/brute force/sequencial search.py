def sequential_search(arr, target):
    for index, element in enumerate(arr):
        if element == target:
            return index  # Return the index of the found element
    return -1  # Return -1 if the element is not found

# Example usage:
arr = [5, 3, 7, 1, 9, 2]
target = 7
result = sequential_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
