arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)

for ind in  range(size):
    min_i = ind
    for j in range(ind+1,size):
        if arr[j]<arr[min_i]:
            min_i=j
    (arr[ind],arr[min_i]) = (arr[min_i],arr[ind])
print(arr)