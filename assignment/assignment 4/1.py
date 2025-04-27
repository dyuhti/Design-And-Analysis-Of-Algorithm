words = ["adc", "wxy", "abc"]
w =[]
letter_values = {chr(i): i - 97 for i in range(97, 123)}
for word in words:
    wdiff=[]
    for i in range(len(word)-1):
        diff = letter_values[word[i+1]] - letter_values[word[i]]
        wdiff.append(diff)
    w.append(wdiff)

# List of words
words = ["adc", "wxy", "abc"]

# Define the letter values
letter_values = {chr(i): i - 97 for i in range(97, 123)}

# Initialize a list to store the differences for each word
w = []

# Calculate the differences for each word
for word in words:
    wdiff = []
    for i in range(len(word) - 1):
        diff = letter_values[word[i + 1]] - letter_values[word[i]]
        wdiff.append(diff)
    w.append(wdiff)

# Print the differences
print("Differences for each word:", w)

# Find the unique difference array
unique_diff = [diff for diff in w if w.count(diff) == 1][0]

# Find the corresponding word for the unique difference array
unique_word = words[w.index(unique_diff)]

# Print the unique word
print("The odd word out is:", unique_word)


