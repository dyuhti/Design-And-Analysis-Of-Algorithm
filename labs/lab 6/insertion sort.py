ar = [9, 5, 1, 4, 3]
for step in range(1, len(ar)):
    key = ar[step]
    j = step - 1
    while j >= 0 and key < ar[j]:
        ar[j + 1] = ar[j]
        j = j - 1
    ar[j + 1] = key
print(ar)
