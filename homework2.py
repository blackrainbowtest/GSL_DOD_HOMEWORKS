def is_curzon(num):
    return (2 ** num + 1) % (2 * num + 1) == 0


print(is_curzon(1025))
print(is_curzon(14))
