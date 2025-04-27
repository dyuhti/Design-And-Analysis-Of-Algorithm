def find(arr, low, high):
    if low == high:
        return arr[low], arr[high]
    if high == low + 1:
        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    mid = (low + high) // 2
    min1, max1 = find(arr, low, mid)
    min2, max2 = find(arr, mid + 1, high)
    return min(min1,min2) ,max(max1,max2)


arr = [1, 35, 2, 4, 36, 2, 46, 2]
min, max = find(arr, 0, len(arr) - 1)
print(min,max)
