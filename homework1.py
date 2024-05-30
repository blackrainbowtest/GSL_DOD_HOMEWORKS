def move_zeros(u_list):
    return sorted(u_list, key=lambda x: (x == 0))


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
