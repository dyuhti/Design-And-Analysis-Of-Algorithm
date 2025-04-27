from collections import Counter


def fsort(s):
    freq = Counter(s)
    chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    result = ''.join([char * count for char, count in chars])
    return result

s = "tree"
print(fsort(s))

