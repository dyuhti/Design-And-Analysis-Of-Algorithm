def last_string_before_empty(s):
    while True:
        original_s = s
        for char in set(s):
            s = s.replace(char, '', 1)
        if s == "":
            return original_s
s = "aabcbbca"
print(last_string_before_empty(s))