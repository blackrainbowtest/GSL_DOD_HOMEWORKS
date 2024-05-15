while True:
    try:
        user_input = input('Enter numbers separated by spaces: ')
        user_array = [int(i) for i in user_input.split()]
        print(f'Max: {max(user_array)}, Min: {min(user_array)}')
        break
    except ValueError:
        print("Please enter valid numbers separated by spaces.")
