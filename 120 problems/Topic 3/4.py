c=0
def merge_sort(array):
    global c
    if len(array) >1:
        r=len(array)//2
        L =array[:r]
        M = array[r:]

        merge_sort(L)
        merge_sort(M)

        i=j=k=0

        while i<len(L) and j <len(M):
            c+=1
            if L[i] < M[j]:
                array[k]=L[i]
                i+=1
            else:
                array[k]=M[j]
                j+=1
            k+=1

            while i <len(L):
                array[k]=L[i]
                i+=1
                k+=1

            while j <len(M):
                array[k]= M[j]
                j+=1
                k+=1

def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


array = [6, 5, 12, 10, 9, 1]

merge_sort(array)

print("Sorted array is: ")
printList(array)
print(c)