def kidsWithCandies(candies, extraCandies):
    max_candies = max(candies)
    result = [candy + extraCandies >= max_candies for candy in candies]
    return result

# Example usage:
candies = [2,3,5,1,3]
extraCandies = 3
print(kidsWithCandies(candies, extraCandies))  # Output: [True, True, True, False, True]

candies = [4,2,1,1,2]
extraCandies = 1
print(kidsWithCandies(candies, extraCandies))  # Output: [True, False, False, False, False]

candies = [12,1,12]
extraCandies = 10
print(kidsWithCandies(candies, extraCandies))  # Output: [True, False, True]