import unittest
from digits_between_0_and_x import digits_between_0_and_x

class TestDigitsBetween0AndX(unittest.TestCase):
    """
    Test cases for the digits_between_0_and_x function.
    Function should return the total count of digits from 0 to x.
    Following TDD principles: Write tests first, then implement the function.
    """
    
    def test_single_digit_number(self):
        """Test with 1 - should return 0 (no digits from 0 to 1)"""
        result = digits_between_0_and_x(1)
        expected = 0
        self.assertEqual(result, expected)
    
    def test_double_digit_number(self):
        """Test with 10 - should return 9"""
        result = digits_between_0_and_x(10)
        expected = 9
        self.assertEqual(result, expected)
    
    def test_triple_digit_number(self):
        """Test with 100 - should return 189"""
        result = digits_between_0_and_x(100)
        expected = 189
        self.assertEqual(result, expected)
    
    def test_four_digit_number(self):
        """Test with 2020 - should return 6969"""
        result = digits_between_0_and_x(2020)
        expected = 6969
        self.assertEqual(result, expected)
    
if __name__ == '__main__':
    unittest.main() 