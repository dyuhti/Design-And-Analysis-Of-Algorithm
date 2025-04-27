#Non-Recursive Algorithm: Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Mathematical Analysis:
# Time Complexity: O(n)
# Space Complexity: O(1)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
result = linear_search(arr, target)
if result!= -1:
    print("Element found at index", result)
else:
    print("Element not found")

#Recursive Algorithm: Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Mathematical Analysis:
# Time Complexity: O(n)
# Space Complexity: O(n) (due to recursive call stack)

n = 5
result = factorial(n)
print("Factorial of", n, "is", result)