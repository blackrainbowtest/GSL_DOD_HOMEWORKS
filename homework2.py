import re
from datetime import datetime

date_pattern = r'(\d{4})[./-](\d{2})[./-](\d{2})\s(\d{2}):(\d{2}):(\d{2})'
while True:
    u_date1 = input('Enter first date (YYYY-MM-DD HH:MM:SS) (or "q" to quit): ')
    u_date2 = input('Enter second date (YYYY-MM-DD HH:MM:SS) (or "q" to quit): ')
    if u_date1.lower() == 'q' or u_date2.lower() == 'q':
        break
    try:
        match1 = re.match(date_pattern, u_date1)
        match2 = re.match(date_pattern, u_date2)
        if match1 and match2:
            # use map(int, tuple) to change all values type and use tuple unpacking
            year1, month1, day1, hour1, minute1, second1 = map(int, match1.groups())
            year2, month2, day2, hour2, minute2, second2 = map(int, match2.groups())
            date_time1 = datetime(year1, month1, day1, hour1, minute1, second1)
            date_time2 = datetime(year2, month2, day2, hour2, minute2, second2)
            # Difference between dates
            difference = date_time2 - date_time1
            print("Difference is:", difference)
        else:
            print('One or both of the dates are in the incorrect format, try again.')
    except ValueError:
        print('Uncorrected input, try again.')
