import unittest
import math

from circle import area as circle_area, perimeter as circle_perimeter
from rectangle import area as rectangle_area, perimeter as rectangle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter

class TestCircle(unittest.TestCase):
    """тесты для функций круга"""
    
    def test_circle_area_positive_radius(self):
        """тест площади круга с положительным радиусом"""
        self.assertAlmostEqual(circle_area(1), math.pi)
        self.assertAlmostEqual(circle_area(2), 4 * math.pi)
        self.assertAlmostEqual(circle_area(5), 25 * math.pi)
    
    def test_circle_area_zero_radius(self):
        """тест площади круга с нулевым радиусом"""
        self.assertEqual(circle_area(0), 0)
    
    def test_circle_area_negative_radius(self):
        """тест площади круга с отрицательным радиусом"""
        with self.assertRaises(ValueError):
            circle_area(-1)
    
    def test_circle_perimeter_positive_radius(self):
        """тест периметра круга с положительным радиусом"""
        self.assertAlmostEqual(circle_perimeter(1), 2 * math.pi)
        self.assertAlmostEqual(circle_perimeter(3), 6 * math.pi)
        self.assertAlmostEqual(circle_perimeter(10), 20 * math.pi)
    
    def test_circle_perimeter_zero_radius(self):
        """тест периметра круга с нулевым радиусом"""
        self.assertEqual(circle_perimeter(0), 0)
    
    def test_circle_perimeter_negative_radius(self):
        """тест периметра круга с отрицательным радиусом"""
        with self.assertRaises(ValueError):
            circle_perimeter(-5)


class TestRectangle(unittest.TestCase):
    """тесты для функций прямоугольника"""
    
    def test_rectangle_area_positive_sides(self):
        """тест площади прямоугольника с положительными сторонами"""
        self.assertEqual(rectangle_area(2, 3), 6)
        self.assertEqual(rectangle_area(5, 5), 25)
        self.assertEqual(rectangle_area(10, 4), 40)
    
    def test_rectangle_area_zero_side(self):
        """тест площади прямоугольника с нулевой стороной"""
        self.assertEqual(rectangle_area(0, 5), 0)
        self.assertEqual(rectangle_area(5, 0), 0)
        self.assertEqual(rectangle_area(0, 0), 0)
    
    def test_rectangle_area_negative_sides(self):
        """тест площади прямоугольника с отрицательными сторонами"""
        with self.assertRaises(ValueError):
            rectangle_area(-2, 3)
        with self.assertRaises(ValueError):
            rectangle_area(2, -3)
        with self.assertRaises(ValueError):
            rectangle_area(-2, -3)
    
    def test_rectangle_perimeter_positive_sides(self):
        """тест периметра прямоугольника с положительными сторонами"""
        self.assertEqual(rectangle_perimeter(2, 3), 10)
        self.assertEqual(rectangle_perimeter(5, 5), 20)
        self.assertEqual(rectangle_perimeter(10, 4), 28)
    
    def test_rectangle_perimeter_zero_side(self):
        """тест периметра прямоугольника с нулевой стороной"""
        self.assertEqual(rectangle_perimeter(0, 5), 10)
        self.assertEqual(rectangle_perimeter(5, 0), 10)
        self.assertEqual(rectangle_perimeter(0, 0), 0)
    
    def test_rectangle_perimeter_negative_sides(self):
        """тест периметра прямоугольника с отрицательными сторонами"""
        with self.assertRaises(ValueError):
            rectangle_perimeter(-2, 3)
        with self.assertRaises(ValueError):
            rectangle_perimeter(2, -3)


class TestSquare(unittest.TestCase):
    """тесты для функций квадрата"""
    
    def test_square_area_positive_side(self):
        """тест площади квадрата с положительной стороной"""
        self.assertEqual(square_area(2), 4)
        self.assertEqual(square_area(5), 25)
        self.assertEqual(square_area(10), 100)
    
    def test_square_area_zero_side(self):
        """тест площади квадрата с нулевой стороной"""
        self.assertEqual(square_area(0), 0)
    
    def test_square_area_negative_side(self):
        """тест площади квадрата с отрицательной стороной"""
        with self.assertRaises(ValueError):
            square_area(-3)
    
    def test_square_perimeter_positive_side(self):
        """тест периметра квадрата с положительной стороной"""
        self.assertEqual(square_perimeter(2), 8)
        self.assertEqual(square_perimeter(5), 20)
        self.assertEqual(square_perimeter(10), 40)
    
    def test_square_perimeter_zero_side(self):
        """тест периметра квадрата с нулевой стороной"""
        self.assertEqual(square_perimeter(0), 0)
    
    def test_square_perimeter_negative_side(self):
        """тест периметра квадрата с отрицательной стороной"""
        with self.assertRaises(ValueError):
            square_perimeter(-4)


class TestTriangle(unittest.TestCase):
    """тесты для функций треугольника"""
    
    def test_triangle_area_positive_values(self):
        """тест площади треугольника с положительными значениями"""
        self.assertEqual(triangle_area(2, 3), 3.0)
        self.assertEqual(triangle_area(5, 4), 10.0)
        self.assertEqual(triangle_area(10, 6), 30.0)
    
    def test_triangle_area_zero_values(self):
        """тест площади треугольника с нулевыми значениями"""
        self.assertEqual(triangle_area(0, 5), 0)
        self.assertEqual(triangle_area(5, 0), 0)
        self.assertEqual(triangle_area(0, 0), 0)
    
    def test_triangle_area_negative_values(self):
        """тест площади треугольника с отрицательными значениями"""
        with self.assertRaises(ValueError):
            triangle_area(-2, 3)
        with self.assertRaises(ValueError):
            triangle_area(2, -3)
    
    def test_triangle_perimeter_positive_sides(self):
        """тест периметра треугольника с положительными сторонами"""
        self.assertEqual(triangle_perimeter(2, 3, 4), 9)
        self.assertEqual(triangle_perimeter(5, 5, 5), 15)
        self.assertEqual(triangle_perimeter(10, 6, 8), 24)
    
    def test_triangle_perimeter_zero_sides(self):
        """тест периметра треугольника с нулевыми сторонами"""
        self.assertEqual(triangle_perimeter(0, 3, 4), 7)
        self.assertEqual(triangle_perimeter(2, 0, 4), 6)
        self.assertEqual(triangle_perimeter(2, 3, 0), 5)
        self.assertEqual(triangle_perimeter(0, 0, 0), 0)
    
    def test_triangle_perimeter_negative_sides(self):
        """тест периметра треугольника с отрицательными сторонами"""
        with self.assertRaises(ValueError):
            triangle_perimeter(-2, 3, 4)
        with self.assertRaises(ValueError):
            triangle_perimeter(2, -3, 4)


if __name__ == '__main__':
    unittest.main()