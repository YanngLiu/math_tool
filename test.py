"""Module test provides unit test."""

import unittest

import util

class Test(unittest.TestCase):
    """Test representing a unit test for util"""
    def test_factors(self):
        """Function test_factors."""
        self.assertEqual(util.factors(4), {2:2})
        self.assertEqual(util.factors(12), {2:2,3:1})
        self.assertEqual(util.factors(10000), {2:4,5:4})
        self.assertEqual(util.factors(2100000000), {2:8,5:8,3:1,7:1})
    def test_is_prime(self):
        """Function test_is_prime."""
        self.assertFalse(all(util.is_prime(x) for x in [4,8,9]))
        self.assertTrue(all(util.is_prime(x) for x in [2,3,13,23]))
    def test_perfect_square(self):
        """Function test_perfect_square."""
        self.assertTrue(all(util.is_perfect_square(x) for x in [4,9,235*235]))
        self.assertFalse(all(util.is_perfect_square(x) for x in [8,10,235*234]))
    def test_perfect_cubic(self):
        """Function test_perfect_cubic."""
        self.assertTrue(all(util.is_perfect_cubic(x) for x in [8,235*235*235]))
        self.assertFalse(all(util.is_perfect_cubic(x) for x in [10,235*234]))

if __name__ == '__main__':
    unittest.main()
