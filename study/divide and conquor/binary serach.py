def binary_search(arr,target):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low = mid+1
        else:
            high = mid-1

    return -1

arr=[1,3,3,5,2,52,53,24]
target=52
result = binary_search(arr,target)
print(result)