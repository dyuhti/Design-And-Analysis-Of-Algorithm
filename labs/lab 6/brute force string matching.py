text = "this is a simple example"
pattern = "simple"
matches=[]
n = len(text)
m = len(pattern)
for i in range(n-m+1):
    match = True
    for j in range(m):
        if text[i + j] != pattern[j]:
            match = False
            break
    if match:
        matches.append(i)
print(matches)
