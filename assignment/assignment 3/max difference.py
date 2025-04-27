def maxDiff(num):
    num_str = str(num)
    max_num = num_str[:]
    min_num = num_str[:]

    # Find the maximum possible number
    for i in range(10):
        max_num = max_num.replace(str(i), '9')
        if max_num != '0':
            break

    # Find the minimum possible number
    if min_num[0] != '1':
        min_num = min_num.replace(min_num[0], '1')
    else:
        for i in range(1, len(min_num)):
            if min_num[i] != '0' and min_num[i] != min_num[0]:
                min_num = min_num.replace(min_num[i], '0')
                break

    return int(max_num) - int(min_num)

# Example usage
print(maxDiff(555))  # Output: 888

