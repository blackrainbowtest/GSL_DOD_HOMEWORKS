import re


def mask_number(number: str) -> str:
    masked_result = []
    dig_count = 0

    for char in reversed(number):
        if char.isdigit():
            if dig_count >= 4:
                masked_result.append("*")
            else:
                masked_result.append(char)
            dig_count += 1
        else:
            masked_result.append(char)
    masked_result.reverse()

    return "".join(masked_result)


print(mask_number("1234 5678 1234 5678"))
print(mask_number("52310259"))
