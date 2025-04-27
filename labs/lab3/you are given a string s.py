def last_string_before_empty(s):
    # List to keep track of the last occurrences in order
    result = []

    # Iterate over the string in reverse
    for char in reversed(s):
        # If the character is not already in the result, add it
        if char not in result:
            result.append(char)

    # Reverse the result list to get the correct order
    result.reverse()

    # Return the resulting string formed by the last occurrences
    return ''.join(result)

# Example
initial_s = "aabcbbca"
result = last_string_before_empty(initial_s)
print(result)  # Output: "ba"
