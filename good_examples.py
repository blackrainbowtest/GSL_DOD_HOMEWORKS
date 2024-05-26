# Task 1
# vahram

def create():
    str1 = "Euphoria"
    # Cool idea but list starts with 0 index and when we get 8 // 2 == 4 and call strl[4] its a 5th item of list but its ok, bc task description incorrect
    result = str1[0] + str1[len(str1) // 2] + str1[-1]
    print(result.upper())

    print(len(str1) // 2)
    print(len(str1))
create()

# Task 2
# derenik

from datetime import datetime

def days_difference():
    try:
        date_str1 = input("Enter the first date and time (YYYY-MM-DD HH:MM:SS): ")
        date_str2 = input("Enter the first date and time (YYYY-MM-DD HH:MM:SS): ")
        date_format = '%Y-%m-%d %H:%M:%S'

        result1 = datetime.strptime(date_str1, date_format)
        result2 = datetime.strptime(date_str2, date_format)
        final = result2 - result1
        return f"Difference is {final.days} days."
    except ValueError:
        return "Oops! The input is not in correct format."

print(days_difference())
