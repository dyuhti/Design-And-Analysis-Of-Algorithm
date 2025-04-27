def rev(n):
    r=0
    while n>0:
        digit = n%10
        r = r*10 +digit
        n = n//10
    return r
num = 123
print(rev(num))
