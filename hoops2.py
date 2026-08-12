# Polymorphism
# Problem: Calculate different shapes area

class Circle:
    def area(self):
        radius = 5
        return 3.14 * radius * radius


class Square:
    def area(self):
        side = 5
        return side * side


circle = Circle()
square = Square()

print("Circle Area:", circle.area())
print("Square Area:", square.area())