class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def show_area(self):
        return self.length * self.width

    def show_perimeter(self):
        return 2 * (self.length + self.width)

    def scale(self, factor):
        self.length *= factor
        self.width *= factor


rectangle = Rectangle(4, 3)

print("Length:", rectangle.length)
print("Width:", rectangle.width)
print("Area:", rectangle.show_area())
print("Perimeter:", rectangle.show_perimeter())

# Масштабирование прямоугольника
rectangle.scale(2)

print("After scaling:")
print("Length:", rectangle.length)
print("Width:", rectangle.width)
print("Area:", rectangle.show_area())
print("Perimeter:", rectangle.show_perimeter())
