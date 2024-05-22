def print_triangle(height):
    # Set triangle height range
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2 * i - 1))  # for symmetry, we use odd numbers


def user_input():
    height = int(input("Enter the height of the triangle:"))
    if height <= 0 or height > 10:  # we set here min and max height
        print("Error: Enter a positive number.")
    else:
        print("Triangle:")
        print_triangle(height)


user_input()