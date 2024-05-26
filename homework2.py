def num_checker(n):
    if 0 < int(n) < 1000:
        return int(n)


while True:
    u_date1 = input('Enter number for check (or "q" to quit): ')
    u_date2 = input('Enter numbers with spaces (or "q" to quit): ')
    u_result = False
    if u_date1.lower() == 'q' or u_date2.lower() == 'q':
        break
    try:
        u_array = list(map(num_checker, u_date2.split(" ")))
        if u_array.__contains__(None):
            break
        for x in u_array:
            for y in u_array:
                if x * y == int(u_date1):
                    u_result = True
                    break
        if u_result:
            print("Yes")
        else:
            print("No")

    except ValueError:
        print('Uncorrected input, try again.')
