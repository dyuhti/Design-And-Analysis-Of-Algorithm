def brute_force_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    occurrences = []

    for i in range(n - m + 1):
        match_found = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match_found = False
                break
        if match_found:
            occurrences.append(i)

    return occurrences

# Example usage:
text = "ababcababcabc"
pattern = "abc"
matches = brute_force_string_match(text, pattern)
print("Pattern matches found at indices:", matches)
