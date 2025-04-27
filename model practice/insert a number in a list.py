def insert_number_in_list(lst, num, position):
    new_list = []
    inserted = False
    for i in range(len(lst)):
        if i == position:
            new_list.append(num)
            inserted = True
        new_list.append(lst[i])

    # If position is beyond the end of the list, append num at the end
    if not inserted:
        new_list.append(num)

    return new_list


# Example usage:
my_list = [1, 2, 3, 4, 5]
number_to_insert = 10
insertion_position = 2  # Index to insert number

new_list = insert_number_in_list(my_list, number_to_insert, insertion_position)
print(f"Original list: {my_list}")
print(f"List after inserting {number_to_insert} at position {insertion_position}: {new_list}")
