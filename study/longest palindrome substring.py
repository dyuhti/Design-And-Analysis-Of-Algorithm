s="teeth"
r=set()

for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        substr = s[i:j]
        if substr == substr[::-1] and len(substr) > 1:
            r.add(substr)
print(max(r,key=len))