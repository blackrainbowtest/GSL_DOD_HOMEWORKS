while True:
    u_input = input('Enter nums with spaces (or "q" to quit): ')
    if u_input.lower() == 'q':
        break
    try:
        u_array = list(map(int, u_input.split(' ')))
        u_array.insert(0, u_array[-1])
        u_array.pop()
        print(u_array)
    except ValueError:
        print('Uncorrected input, try again.')
