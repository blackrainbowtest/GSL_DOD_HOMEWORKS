def switch_variables(u_list, u_pos1, u_pos2):
    if u_pos1 >= len(u_list) or u_pos2 >= len(u_list):
        return 'Out of range'
    u_list[u_pos1], u_list[u_pos2] = u_list[u_pos2], u_list[u_pos1]
    return u_list


print(switch_variables([23, 65, 19, 90], 0, 2))
