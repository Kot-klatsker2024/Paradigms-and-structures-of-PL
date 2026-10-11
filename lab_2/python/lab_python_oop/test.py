import unittest
import math
from Classes import Rectangle, Circle, Square

class TestGeometricFigures(unittest.TestCase):

    def test_rectangle_area(self):
        rect = Rectangle(18, 18, "синий")
        self.assertEqual(rect.calculate_area(), 324)

    def test_square_area(self):
        square = Square(18, "красный")
        self.assertEqual(square.calculate_area(), 324)

    def test_circle_area(self):
        radius = 18
        circle = Circle(radius, "зелёный")
        expected_area = (radius ** 2) * math.pi
        self.assertEqual(circle.calculate_area(), expected_area)

    def test_figure_names(self):
        rect = Rectangle(2, 2, "белый")
        self.assertEqual(rect.get_name(), "Прямоугольник\n")

if __name__ == '__main__':
    unittest.main()
