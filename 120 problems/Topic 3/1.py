def maxx(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        mid = len(arr) // 2
        left_max = maxx(arr[:mid])
        right_max = maxx(arr[mid:])
        return max(left_max, right_max)


def minn(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        mid = len(arr) // 2
        left_minn = minn(arr[:mid])
        right_minn = minn(arr[mid:])
        return min(left_minn, right_minn)


arr = [2, 3, 1, 3, 15, 7, 9, 4]
print("Maximum element :", maxx(arr))
print("Minimum element : ", minn(arr))
