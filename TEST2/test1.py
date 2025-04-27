s = "ababbc"
k = 2
c = 0

for i in range(len(s)):
    for j in range(i, len(s)-i-1):
        if s[i] == s[j] and c<=k :
            c += 1
        else:
            continue
print(c)
