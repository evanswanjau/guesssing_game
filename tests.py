"""
Tests for our guessing gaming
"""
import unittest
import app

class TestGuessingGame(unittest.TestCase):
    """
    Test all functions involved in the guessing game
    """
    def test_input(self):
        """
        Function to test our input
        1. Must return an integer
        2. Must ne a range of 0 - 10
        """
        self.assertEqual(app.get_input_value(), 5)
        self.assertIsInstance(app.get_input_value(), int)

    def test_random_value(self):
        """
        Function to test our random value
        1. Must be an integer
        2. Must be between greater than 0
        3. Must be less than 11
        """
        self.assertIsInstance(app.get_random_value(), int)
        self.assertGreater(app.get_random_value(), 0)
        self.assertLess(app.get_random_value(), 11)

if __name__ == '__main__':
    unittest.main()