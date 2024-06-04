def sorted_words():
    u_input = input('Enter words with spaces: >>> ')
    u_list = u_input.split()
    u_list.sort(key=lambda x: len(x))

    return u_list


print(sorted_words())
