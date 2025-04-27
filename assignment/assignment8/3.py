from collections import defaultdict

nums = [4, 8, 3, 6, 12, 9]
space = 4

rem_c = defaultdict(int)
for num in nums:
    rem = num % space
    rem_c[rem] += 1

max_targets = max(rem_c.values())
candidates = [num for num in nums if rem_c[num % space] == max_targets]

print(min(candidates))