def partition(array,low,high):
    pivot =array[high]
    i=low-1
    for j in range(low,high):
        if array[j]<=pivot:
            i=i+1
        (array[i],array[j])=(array[j],array[i])
    (array[i+1],array[high]) = (array[high],array[i+1])

def quick(array,low,high):
    if low<high:
        par = partition(array,low,high)
        quick(array,low,par-1)
        quick(array,par+1,high)

data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quick(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)