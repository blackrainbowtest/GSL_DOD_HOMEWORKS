def pascal_triangle(n):
    row = [1]
    y = [0]
    for _ in range(max(n, 0)):
        print(row)
        row = list(left + right for left, right in zip(row + y, y + row))


pascal_triangle(8)
