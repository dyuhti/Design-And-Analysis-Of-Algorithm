ar = [20, 12, 10, 15, 2]



def selection(ar, size):
    for step in range(size):
        ele = step

        for i in range(step + 1, size):
            if ar[i] < ar[ele]:
                ele = i

        (ar[step], ar[ele]) = (ar[ele], ar[step])


selection(ar, len(ar))
print(ar)
