import unittest
from src.circle_mastri.calculate import calculate_area, calculate_circumference


class TestCalculations(unittest.TestCase):

    def test_circumference_calculations(self):
        self.assertEqual(round(calculate_circumference(5), 3), 31.416)

    def test_circumference_with_negative_radius(self):
        self.assertRaises(ValueError, calculate_circumference, -1)

    def test_area_calculations(self):
        self.assertEqual(round(calculate_area(5), 3), 78.540)

    def test_area_with_negative_radius(self):
        self.assertRaises(ValueError, calculate_area, -1)

    def test_circumference_from_zero(self):
        self.assertEqual(calculate_circumference(0), 0)

    def test_area_from_zero(self):
        self.assertEqual(calculate_area(0), 0)
