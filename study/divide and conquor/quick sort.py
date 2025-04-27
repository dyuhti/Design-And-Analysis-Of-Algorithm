def quick(arr):
    if len(arr)<=1:
        return arr
    else:
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x<pivot]
        middle=[x for x in arr if x==pivot]
        right = [x for x in arr if x>pivot]
        return quick(left)+middle+quick(right)

arr=[3,6,8,10,1,12,1]
sorted_arr = quick(arr)
print(sorted_arr)