def find_odd_string(words):
    for word in words:
        diff_array = [ord(word[i + 1]) - ord(word[i]) for i in range(len(word) - 1)]
        count = 0
        for w in words:
            if w != word:
                if [ord(w[i + 1]) - ord(w[i]) for i in range(len(w) - 1)] == diff_array:
                    count += 1
        if count == 0:
            return word


words1 = ["adc", "wzy", "abc"]
words2 = ["aaa", "bob", "ccc", "ddd"]
print(find_odd_string(words1))
print(find_odd_string(words2))