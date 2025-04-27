def minimize_string_value(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(s)):
        if s[i] == '?':
            counts = [s[:i].count(letter) for letter in alphabet]
            s = s[:i] + alphabet[counts.index(min(counts))] + s[i + 1:]
    return s


# Example
s = "a?b?c?"
result = minimize_string_value(s)
print(result)
