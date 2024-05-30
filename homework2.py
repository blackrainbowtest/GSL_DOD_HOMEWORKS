# a2 + b2 == c2 pythagorean
# we know that c - b == diff, we can get c by c == diff + b
# a^2 + b^2 == c^2 <==> a^2 + b^2 == diff^2 + 2(diff * b) + b^2
# a^2 == diff^2 + 2diff * b =>> to find b  |  (a2 - diff2) / 2 diff == b

def get_pythagorean_triples(diff, low, high):
    if diff > 9999:
        return 'diff is > 9999!'
    if low > high:
        low, high = high, low
    if high > 9999999:
        return 'high is > 9999999!'
    if diff <= 0:
        return 'diff is <= 0!'

    triples = []

    for a in range(low, high + 1):  # smallest side is a
        a_2 = a * a
        diff_2 = diff * diff
        b = (a_2 - diff_2) / (2 * diff)
        if b.is_integer() and b > 0:
            b = int(b)
            c = b + diff
            if a * a + b * b == c * c:
                triples.append((a, b, c))

        pass

    return triples


print(get_pythagorean_triples(1, 2, 10))
print(get_pythagorean_triples(3, 10, 25))
