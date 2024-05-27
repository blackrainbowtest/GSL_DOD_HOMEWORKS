def sum_func(num_list):
    max_num = float('-inf')  # set max_num
    current_num = 0

    for num in num_list:
        current_num = max(current_num + num, num)
        max_num = max(current_num, max_num)

    return max_num


u_nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(sum_func(u_nums))
