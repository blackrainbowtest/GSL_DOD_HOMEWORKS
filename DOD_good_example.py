def check_leap(year):
    if (year % 400 == 0) and (year % 100 == 0):
        return True

    elif (year % 4 == 0) and (year % 100 != 0):
        return True

    else:
        return False


print(check_leap(2000))
print(check_leap(2400))
print(check_leap(1800))
print(check_leap(2200))
print(check_leap(2500))
print(check_leap(2016))
