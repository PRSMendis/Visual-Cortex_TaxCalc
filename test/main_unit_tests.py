import unittest
from main import calculator
from tax_data import tax_dict, str_map


class TestTCalculator(unittest.TestCase):
    def test_small(self):
        for (a, b) in [calculator(96200, tax_dict[2020]),  21732]:
            self.assertEqual(a, b)
