def intersection_of_three_arrays(arr1, arr2, arr3):
    result = []
    p1, p2, p3 = 0, 0, 0

    while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
        if arr1[p1] == arr2[p2] == arr3[p3]:
            result.append(arr1[p1])
            p1 += 1
            p2 += 1
            p3 += 1
        elif arr1[p1] < arr2[p2]:
            p1 += 1
        elif arr2[p2] < arr3[p3]:
            p2 += 1
        else:
            p3 += 1

    return result


# Example usage
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]
print("Example 1 Output:", intersection_of_three_arrays(arr1, arr2, arr3))  # Output: [1, 5]

arr1 = [197, 418, 523, 876, 1356]
arr2 = [501, 880, 1593, 1710, 1870]
arr3 = [521, 682, 1337, 1395, 1764]
print("Example 2 Output:", intersection_of_three_arrays(arr1, arr2, arr3))  # Output: []
