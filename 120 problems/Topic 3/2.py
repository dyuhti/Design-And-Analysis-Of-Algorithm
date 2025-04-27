def max_ele(ar, n):
    if n == 1:
        return ar[0]
    else:
        mid = n // 2
        left_max = max_ele(ar[:mid], mid)
        right_max = max_ele(ar[mid:], n - mid)
        return max(left_max, right_max)
def min_ele(ar, n):
    if n == 1:
        return ar[0]
    else:
        mid = n // 2
        left_min = min_ele(ar[:mid], mid)
        right_min = min_ele(ar[mid:], n - mid)
        return min(left_min, right_min)
n = 8
ar = [5, 10, 4, 25, 70, 56, 2, 96]
print("min element", min_ele(ar, n))
print("max element", max_ele(ar, n))