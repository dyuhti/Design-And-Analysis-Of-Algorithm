def string(a, b):
    s = []

    while a > 0 or b > 0:
        if a > b:
            if len(s) >= 2 and s[-1] == s[-2] == 'a':
                s.append('b')
                b -= 1
            else:
                s.append('a')
                a -= 1
        elif b > a:
            if len(s) >= 2 and s[-1] == s[-2] == 'b':
                s.append('a')
                a -= 1
            else:
                s.append('b')
                b -= 1
        else:
            if len(s) >= 2 and s[-1] == s[-2]:
                if s[-1] == 'a':
                    s.append('b')
                    b -= 1
                else:
                    s.append('a')
                    a -= 1
            else:
                s.append('a')
                a -= 1
    return ''.join(s)


print(string(1, 2))
