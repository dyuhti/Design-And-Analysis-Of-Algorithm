import math

num = [3, 6, 2, 7, 1]
k = 6
count = 0

size = len(num)-1
for i in range(size):
    if num[i] == k:
        count += 1
    for j in range(i+1, size):
        if math.lcm(num[i], num[j]) == k:
            count += 1
print(count)