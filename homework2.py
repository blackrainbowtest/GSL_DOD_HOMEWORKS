import random
import string


def generate_password(length=8):
    if length < 8:
        length = 8

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()_+=-"
    password_required = [random.choice(lower), random.choice(upper), random.choice(digits), random.choice(symbols)]
    random.shuffle(password_required)

    for _ in range(len(password_required), length):
        password_required.append(random.choice(lower + upper + digits + symbols))

    random.shuffle(password_required)
    return ''.join(password_required)


print(generate_password(2))
print(generate_password(12))
