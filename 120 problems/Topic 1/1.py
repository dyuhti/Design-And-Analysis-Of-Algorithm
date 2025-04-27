words = ["abc","car","ada","racecar","cool"]
for word in words:
    if word[::-1] == word:
        print(word)
        break