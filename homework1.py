import math

while True:
    u_input = input('Enter your word (or "q" to quit): ')
    if u_input.lower() == 'q':
        break
    try:
        # On input Euphoria we get EHA (not EOA) bc len() - 1 == [-1]
        new_str = u_input[0] + u_input[math.ceil(len(u_input) / 2) - 1] + u_input[-1]
        print(new_str.upper())
    except ValueError:
        print('Uncorrected input, try again.')
