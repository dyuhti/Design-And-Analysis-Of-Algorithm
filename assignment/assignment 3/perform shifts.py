s = "abc"
shift = [[0, 1], [1, 2]]

def left(a, s):
    return s[a:] + s[:a]

def right(a, s):
    return s[-a:] + s[:-a]

while len(shift):
    direction, amount = shift.pop(0)
    if direction == 0:
        s = left(amount, s)
    else:
        s = right(amount, s)

print(s)  # Output: "cab"