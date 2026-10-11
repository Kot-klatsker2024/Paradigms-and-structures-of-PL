import math
from abc import ABC, abstractmethod

class Geometric_figure(ABC):

    @abstractmethod
    def calculate_area(self):
        pass


class Figure_color:
    def __init__(self, name_color):
        self._color = name_color


    @property
    def color(self):
        return self._color

class Rectangle(Geometric_figure):
    def __init__(self, width, height, color):
        self._width = width
        self._height = height
        self._color = Figure_color(color)
        self._name = "Прямоугольник\n"

    def calculate_area(self):
        return self._width * self._height

    def __repr__(self):
        template = ("""Основные параметры:\n\t-длина: {}\n\t-ширина: {}\n\t-цвет: {}\n\t-площадь {}\n""")

        return template.format(
            self._height,
            self._width,
            self._color.color,
            self.calculate_area()
        )

    def get_name(self):
        return self._name

class Circle(Geometric_figure):
    def __init__(self, radius, color):
        self._radius = radius
        self._circ_color = Figure_color(color)
        self._name = "Круг\n"

    def calculate_area(self):
        return ((self._radius)**2) * math.pi

    def __repr__(self):
        template = ("""Основные параметры:\n\t-радиус:{}\n\t-цвет: {}\n\t-площадь {}\n""")

        return template.format(
            self._radius,
            self._circ_color.color,
            self.calculate_area()
        )

    def get_name(self):
        return self._name

class Square(Rectangle):
    def __init__(self, lenght, color):

        super().__init__(lenght, lenght, color)

        self._name = "Квадрат\n"

    def __repr__(self):
        template = ("""Основные параметры:\n\t-сторона: {}\n\t-цвет: {}\n\t-площадь {}\n""")

        return template.format(
            self._height,
            self._color.color,
            self.calculate_area()

        )

    def get_name(self):
        return self._name
