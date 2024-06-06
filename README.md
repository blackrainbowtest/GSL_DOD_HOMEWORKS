Assignment:

Description:
Create a Rectangle class that will represent a rectangle. Realize the methods for calculating the area and perimeter of the rectangle, as well as the method for scaling (change sizes factor).

Requirements:
Rectangle class:
Attributes: 
(Length) - length, 
(width) - width.
Methods:
(__init__) - designer, 
(show_area) - Method for calculating the area.
(show_perimeter) - The method for calculating the perimeter.
(scale) - The method for scaling sizes (use factor to change sizes).

Demonstration of work:

rectangle = Rectangle(4, 3)
print("Length:", rectangle.length)
print("Width:", rectangle.width)
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())

rectangle.scale(2)
print("Length:", rectangle.length)
print("Width:", rectangle.width)
print("Area:", rectangle.area())
print("Perimeter:", rectangle.perimeter())
Assignment: Zoo Simulation

Description:
Create a zoo simulation with various animals. Each animal must have common characteristics and methods, as well as unique characteristics and behaviors. You need to create classes that model the zoo and its inhabitants, and then write code that demonstrates how they interact.

Requirements:
Basic class Animal:
Attributes: 
(name) - name, 
(age) - age, 
(weight) - weight.
Methods: 
(__init__) - designer, 
(show_info) - method for displaying information about the animal,
(make_sound) - the method of sounding.

Subclasses for different types of animals:
For example: Lion, Elephant, Monkey.
Override the (make_sound) method for each animal type.

Zoo class:
Attributes: 
(NAME) - the name of the zoo, 
(animals) - the list [... ,... ,...] of animals.
Methods: 
(add_animal) - adding an animal to the zoo, 
(remove_animal) - removal of the animal from the zoo, 
(show_all_animals) - display of all animals in the zoo.
Demonstration of work:

Create several animal objects.
Add them to the zoo.
Display information about all animals in the zoo.
Demonstrate the publication of sounds by various animals.

# Demonstration of work
zoo = Zoo ("City Zoo Redux")

lion = Lion ("Alex", 5, 190)
elephant = Elephant ("Dumbo", 10, 5400)
panda = Panda ("Po", 4, 1540)

zoo.add_animal (Lion)
zoo.add_animal (Elephant)
zoo.add_animal (Panda)

zoo.show_all_animals ()

zoo.remove_animal (elephant)

