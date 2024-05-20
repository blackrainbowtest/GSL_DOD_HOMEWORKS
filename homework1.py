import re


def is_magic(date):
    match = re.match(r'(\d{2})[./-](\d{2})[./-](\d{4})', date)  # When find data return re.match class

    if match:
        day, month, year = match.groups()  # use .groups() method to get our data
        return int(day) * int(month) == int(year[-2:])
    else:
        raise ValueError("Invalid date format")


print(is_magic('10.06.1960'))
