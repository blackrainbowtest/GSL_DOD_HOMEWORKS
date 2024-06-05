def check_len(u_str):
    max_len = 0
    current_str = []
    for letter in list(u_str):
        if letter not in current_str:
            current_str.append(letter)
            print(current_str)
        else:
            if max_len < len(current_str):
                max_len = len(current_str)
            current_str = [letter]
            print(current_str)
    if max_len < len(current_str):
        max_len = len(current_str)
    return max_len


print(check_len("abcabcbb"))
