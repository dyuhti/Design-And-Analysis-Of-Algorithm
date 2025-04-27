s = "abc"
shift = [[0, 1], [1, 2]]

def left(a, s):
    return s[a:] + s[:a]

def right(a, s):
    return s[-a:] + s[:-a]

while shift:
    for i in range(len(shift)):
        if shift[i][0] == 0:
            a = shift[i][1]
            s = left(a, s)
        else:
            b = shift[i][1]
            s = right(b, s)
    shift.pop(0)

print(s)