s = "abaccdbbd"
k = 3
count = 0

for i in range(len(s)):
    for j in range(i + k, len(s) + 1):
        substring = s[i:j]
        if substring == substring[::-1]:
            count += 1

print(count)  # Output: 2