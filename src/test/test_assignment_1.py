import unittest
import math
from src.main.assignment_1 import approximation_algorithm, bisection_method, fixed_point_iteration, newton_raphson_method

class TestAssignment1(unittest.TestCase):
    
    def test_approximation_algorithm(self):
        result = approximation_algorithm(1.5, 0.000001)
        expected = 1.41421
        self.assertAlmostEqual(result, expected, places=5)
    
    def test_bisection_method(self):
        root = bisection_method(1, 2, 20, 0.001)
        expected = 1.3642578125 
        self.assertAlmostEqual(root, expected, places=3)
    
    def test_fixed_point_iteration(self):
        root = fixed_point_iteration(1.5, 25, 0.000001)
        self.assertIsNone(root)
    
    def test_newton_raphson(self):
        root = newton_raphson_method(math.pi/4, 15 * 10**-15, 50)
        expected = 0.7390851332151606
        self.assertAlmostEqual(root, expected, places=5)

if __name__ == '__main__':
    unittest.main()