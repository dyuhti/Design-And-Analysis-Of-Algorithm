def find_max(nums):
    if not nums:
        raise ValueError("The input list is empty")

    max_num = nums[0]

    for num in nums[1:]:
        if num > max_num:
            max_num = num

    return max_num


print(find_max([1, 2, 3, 4, 5]))
print(find_max([7, 7, 7, 7, 7]))
print(find_max([-10, 2, 3, -4, 5]))
