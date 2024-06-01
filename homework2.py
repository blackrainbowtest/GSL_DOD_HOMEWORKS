def is_prime(num, prime_list):
    if num <= 3 or num == 5:
        return True
    elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
        for prime in prime_list:
            if prime * prime > num:
                break
            if num % prime == 0:
                return False
        return True
    return False


def prime_number(end=100, start=2):
    prime_num_list = []
    if start < 2:
        start = 2
    for num in range(start, end + 1):
        if is_prime(num, prime_num_list):
            prime_num_list.append(num)
    return prime_num_list


print(prime_number(100))