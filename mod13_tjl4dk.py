import unittest
from stock_api import validate_symbol, validate_time_series
from chart_generator import validate_chart_type
from utils import validate_date

# Validation functions for test purposes
def is_valid_symbol(symbol):
    return validate_symbol(symbol)

def is_valid_chart_type(chart_type):
    return validate_chart_type(chart_type)

def is_valid_time_series(time_series):
    return validate_time_series(time_series)

def is_valid_date(date_str):
    return validate_date(date_str)

class TestInputValidation(unittest.TestCase):

    def test_valid_symbol(self):
        self.assertTrue(is_valid_symbol("AAPL"))  # Valid symbol
        self.assertFalse(is_valid_symbol("apple"))  # Invalid symbol (lowercase)
        self.assertFalse(is_valid_symbol("APPL123"))  # Invalid symbol (contains numbers)
        self.assertFalse(is_valid_symbol("A"))  # Invalid symbol (too short)
        self.assertFalse(is_valid_symbol("AAPLAPPLE"))  # Invalid symbol (too long)
    
    def test_valid_chart_type(self):
        self.assertTrue(is_valid_chart_type("1"))  # Valid chart type
        self.assertTrue(is_valid_chart_type("2"))  # Valid chart type
        self.assertFalse(is_valid_chart_type("3"))  # Invalid chart type
