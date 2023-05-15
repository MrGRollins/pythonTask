# 3.Создать иерархию классов фигур: квадрат, прямоугольник, треугольник, круг.
#   Каждый класс должен реализовывать следующие методы:
#   •	вычисление площади
#   •	вычисление периметра
#   •	сравнение площади с другой фигурой (больше или меньше)
#   •	сравнение периметра с другой фигурой (больше или меньше)

import math
from abc import ABC

# Figure
class Figure(ABC):
    def __init__(self):
        self.perimeter = 0
        self.square = 0

    def new_parameters(self):
        pass

    def new_perimeter(self):
        pass

    def new_square(self):
        pass

    def perimeter_info(self, other):
        return self.perimeter < other.new_perimeter()

    def square_info(self, other):
        return self.square < other.new_square()

# Прямоугольник
class Rectangle(Figure):
    def __init__(self, width: float, height: float):
        super().__init__()
        assert width > 0 and height > 0, "The rectangle exists"
        self._width = width
        self._height = height

    def new_parameters(self):
        return self._width, self._height

    def new_perimeter(self):
        return (self._width + self._height) * 2

    def new_square(self):
        return self._width * self._height

# Квадрат
class Square(Rectangle):
    def __init__(self, a: float):
        super().__init__()
        self.a = a

    def new_parameters(self):
        return self.a

    def new_perimeter(self):
        return self.a * 4

    def new_square(self):
        return self.a * self.a

# Круг
class Circle(Figure):
    def __init__(self, r: float):
        super().__init__()
        self.r = r

    def new_parameters(self):
        return self.r

    def new_perimeter(self):
        return self.r * 2 * math.pi

    def new_square(self):
        return math.pi * math.sqrt(self.r)

# Треугольник
class Triangle(Figure):
    def __init__(self, a: float, b: float, c: float):
        super().__init__()

        assert a > 0 and b > 0 and c > 0, "The triangle exist"
        assert a < b + c and b < a + c and c < a + b, "The triangle exist"

        self.a = a
        self.b = b
        self.c = c

    def new_parameters(self):
        return self.a, self.b, self.c

    def new_perimeter(self):
        return self.a + self.b + self.c

    def new_square(self):
        h_per = self.perimeter/2
        return math.sqrt(h_per * (h_per - self.a) * (h_per - self.b) * (h_per - self.c))

if __name__ == '__main__':
    fig_rec = Rectangle(4.5, 7.1)
    print(
        '\n',
        "Parameters figure:  \n",
          " • Perimeter: ", fig_rec.new_square(), '\n',
          " • Square: ", fig_rec.new_perimeter(), '\n'
    )
