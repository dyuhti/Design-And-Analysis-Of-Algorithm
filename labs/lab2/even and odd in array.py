ar = []
e = []
o = []
for i in range(1, 11):
    ar.append(i)
ar.sort()
for num in ar:
    if num % 2 == 0:
        e.append(num)
    else:
        o.append(num)
print("Odd numbers", o)
print("even number", e)
