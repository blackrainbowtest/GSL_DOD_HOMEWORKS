while True:
    u_input = input('Enter year (or "q" to quit): ')
    if u_input.lower() == 'q':
        break
    try:
        if not (1 <= int(u_input)):
            print('Enter a positive number.')
        else:
            if int(u_input) % 400 == 0:
                print(True)
            elif int(u_input) % 100 == 0:
                print(False)
            elif int(u_input) % 4 == 0:
                print(True)
            else:
                print(False)
    except ValueError:
        print('Uncorrected input, try again.')
