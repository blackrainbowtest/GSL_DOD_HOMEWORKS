while True:
    u_input = input('Enter num (1-20) (or "q" to quit): ')
    if u_input.lower() == 'q':
        break
    try:
        if not (1 <= int(u_input) <= 20):
            print('Enter the number between 1 and 20.')
        else:
            for num in range(1, int(u_input) + 1):
                print(num * num)
    except ValueError:
        print('Uncorrected input, try again.')
