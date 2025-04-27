s1 = str(input("Enter a string with spaces"))
s = list(s1.split())
l = []
m=0
for c in s:
        if c not in l:
            l.append(c)
            m = max(m,len(l))
        else:
            l=l[l.index(c)+1:]
            l.append(c)

print(len(l))
