queries = ["word", "note", "ants", "wood"]
dictionary = ["wood", "joke", "moat"]

r=[]
for q in queries:
    for d in dictionary:
        if len(q) == len(d):
            c = 0
            for l in range(len(q)):
                if q[l] != d[l]:
                    c+=1
                if c > 2:
                    break

            if c <= 2 :
                r.append(q)
                break
print(r)
