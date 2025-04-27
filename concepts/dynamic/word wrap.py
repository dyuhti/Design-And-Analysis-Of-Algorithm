def word_wrap(text, width):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 > width:
            lines.append(current_line)
            current_line = word
        else:
            if current_line:
                current_line += " "
            current_line += word

    if current_line:
        lines.append(current_line)

    return "\n".join(lines)

text = "This is a very long sentence that needs to be wrapped to a specific width."
width = 30

wrapped_text = word_wrap(text, width)
print(wrapped_text)