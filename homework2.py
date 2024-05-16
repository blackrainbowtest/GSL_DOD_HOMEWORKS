start, end = 100, 200


def get_largest_palindromic(st, en):
    if st < en:
        st, en = en, st
    for current in range(st, en, -1):
        if str(current) == str(current)[::-1]:
            return current
    return None


print(get_largest_palindromic(start, end))
