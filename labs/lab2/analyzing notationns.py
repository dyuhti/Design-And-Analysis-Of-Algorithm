# Example 1: O(n) time complexity
def example1(n):
    for i in range(1, n + 1):
        print("Hello World!!!")

# Example 2: O(log n) time complexity
def example2(n):
    i = 1
    while i <= n:
        print("Hello World!!!")
        i *= 2

# Example 3: O(n^2) time complexity
def example3(n, m):
    for i in range(n):
        for j in range(m):
            print("Hello World!!!")

# Example 4: O(log log n) time complexity
def example4(n):
    i = 2
    while i <= n:
        print("Hello World!!!")
        i **= 2

# Example 5: Exponential Time — O(2^n)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example 6: Quadratic Time — O(n²)
def bubble_sort(data):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]

# Example 7: Big Theta Notation (Θ)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

# Example 8: Small O Notation (o)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

n = 8
m = 5
example1(n)
example2(n)
example3(n, m)
example4(n)
print(fibonacci(5))
data = [9, 1, 7, 6, 2, 8, 5, 3, 4, 0]
bubble_sort(data)
print(data)
data = [9, 1, 7, 6, 2, 8, 5, 3, 4, 0]
merge_sort(data)
print(data)
data = [9, 1, 7, 6, 2, 8, 5, 3, 4, 0]
insertion_sort(data)
print(data)