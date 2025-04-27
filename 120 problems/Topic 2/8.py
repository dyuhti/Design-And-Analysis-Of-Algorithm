words = ["mass","as","hero","superhero"]
l=[]

for i in range(len(words)):
    for j in range(i+1,len(words)):
        if words[i] in words[j] or words[j] in words[i]:
            if len(words[i]) > len(words[j]):
                l.append(words[j])
            else:
                l.append(words[i])
print(l)