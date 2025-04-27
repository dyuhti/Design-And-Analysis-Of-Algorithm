def find_largest_element(arr):
    if not arr:  # Check if the array is empty
        return None

    largest = arr[0]  # Assume the first element is the largest
    for num in arr:
        if num > largest:
            largest = num
    return largest


# Input from user
array = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

# Find the largest element
largest_element = find_largest_element(array)

# Print the result
if largest_element is not None:
    print(f"The largest element in the array is {largest_element}.")
else:
    print("The array is empty.")
