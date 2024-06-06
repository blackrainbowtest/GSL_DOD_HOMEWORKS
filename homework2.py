from datetime import datetime
import re


def time_converter(u_time):
    time_pattern = re.compile(r"^(1[0-2]|0[1-9]):[0-5][0-9]:[0-5][0-9] (AM|PM)$", re.IGNORECASE)

    if not time_pattern.match(u_time):
        print("Incorrect time format.")

    time_12_hour = datetime.strptime(u_time, "%I:%M:%S %p")
    return time_12_hour.strftime("%H:%M:%S")


print(time_converter("12:10:21 AM"))
