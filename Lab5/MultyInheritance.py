from abc import ABC, abstractmethod

# Parent class Shape
class Shape(ABC):
    @abstractmethod
    def __str__(self):
        pass

# Shape2D class
class Shape2D(Shape, ABC):
    @abstractmethod
    def area(self):
        pass

# Shape3D class
class Shape3D(Shape, ABC):
    @abstractmethod
    def volume(self):
        pass

# Square class - Derived from Shape2D
class Square(Shape2D):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2
    
    def __str__(self):
        return f"Square with side length {self.side_length}"

# Triangle class - Derived from Shape2D
class Triangle(Shape2D):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
    def __str__(self):
        return f"Triangle with base {self.base} and height {self.height}"

# Cuboid class - Derived from Shape3D
class Cuboid(Shape3D):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height
    
    def __str__(self):
        return f"Cuboid with length {self.length}, width {self.width}, and height {self.height}"

# Cone class - Derived from Shape3D
class Cone(Shape3D):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return (1/3) * 3.14159 * self.radius**2 * self.height
    
    def __str__(self):
        return f"Cone with radius {self.radius} and height {self.height}"

# Example usage
square = Square(4)
triangle = Triangle(3, 6)
cuboid = Cuboid(4, 5, 6)
cone = Cone(3, 7)

print(f"Area of {square}: {square.area()}")
print(f"Area of {triangle}: {triangle.area()}")
print(f"Volume of {cuboid}: {cuboid.volume()}")
print(f"Volume of {cone}: {cone.volume()}")
