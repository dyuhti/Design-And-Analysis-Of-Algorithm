def merge_sort(array):
    if len(array) > 1:
        r = len(array) // 2
        l = array[:r]
        m = array[r:]

        merge_sort(l)
        merge_sort(m)

        i = j = k = 0
        while i < len(l) and j < len(m):
            if l[i] < m[j]:
                array[k] = l[i]
                i += 1

            else:
                array[k] = m[j]
                j += 1
            k += 1
        while i < len(l):
            array[k] = l[i]
            i += 1
            k += 1
        while j < len(m):
            array[k] = m[j]
            j += 1
            k += 1


def printlist(array):
    for i in range(len(array)):
        print(array[i], end="")
    print()

array = [6, 8, 9, 2, 1, 4]

merge_sort(array)

print("sorted array is:")
printlist(array)
