def is_magic(date):
    day, month, year = date.split('.')
    
    day = int(day)
    month = int(month)
    year = int(year)

    last_two_digits = year % 100

    if day * month == last_two_digits:
        return True
    else:
        return False

# Test
print(is_magic('10.06.1960'))
print(is_magic('11.06.1960'))
