def kidsWithCandies(candies, extraCandies):
    # Find the maximum number of candies among all kids
    max_candies = max(candies)

    # Initialize the result array
    result = []

    # Iterate through each kid's candies
    for candy in candies:
        # Check if the kid can have the greatest number of candies after adding extraCandies
        result.append(candy + extraCandies >= max_candies)

    return result


# Example usage
print(kidsWithCandies([2, 3, 5, 1, 3], 3))  # Output: [True, True, True, False, True]
print(kidsWithCandies([4, 2, 1, 1, 2], 1))  # Output: [True, False, False, False, False]
print(kidsWithCandies([12, 1, 12], 10))  # Output: [True, False, True]
