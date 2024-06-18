from typing import Protocol


class Shape(Protocol):
    def area(self) -> float:
        ...

    def perimeter(self) -> float:
        ...


class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.141592653589793 * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * 3.141592653589793 * self.radius


def print_shape_info(shape: Shape) -> None:
    print(f'Area: {shape.area()}')
    print(f'Perimeter: {shape.perimeter()}')


rectangle = Rectangle(width=3.0, height=4.0)
circle = Circle(radius=5.0)

print_shape_info(rectangle)
print_shape_info(circle)
