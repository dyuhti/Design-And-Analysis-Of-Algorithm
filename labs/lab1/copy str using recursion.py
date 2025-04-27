def copy_string(source, destination, index=0):
    if index >= len(source):
        return destination

    destination += source[index]

    return copy_string(source, destination, index + 1)


source_string = "Hello, world!"
destination_string = ""
copied_string = copy_string(source_string, destination_string)
print(copied_string)


