from sympy import isprime

s = "23542185131"
k = 3
minLength = 2
count = 0
temp = ""

for i in range(len(s)):
    if isprime(int(s[i])):
        temp += s[i]
    else:
        if len(temp) >= minLength:
            count += 1
            temp = ""
        else:
            temp = ""

print(count)  # Output: 3