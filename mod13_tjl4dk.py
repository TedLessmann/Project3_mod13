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

# only one function is needed to check if an entered date is valid
def is_valid_date(date_str):
    return validate_date(date_str)

class TestInputValidation(unittest.TestCase):

    def test_valid_symbol(self):
        self.assertTrue(is_valid_symbol("AAPL"))  # Valid symbol
        self.assertFalse(is_valid_symbol("apple"))  # Invalid symbol (lowercase)
        self.assertFalse(is_valid_symbol("AAPL123"))  # Invalid symbol (contains numbers)
        self.assertFalse(is_valid_symbol("AAPLAPPL"))  # Invalid symbol (too long)
        self.assertFalse(is_valid_symbol(None))  # Invalid symbol (null)
    
    def test_valid_chart_type(self):
        self.assertTrue(is_valid_chart_type("1"))  # Valid chart type
        self.assertTrue(is_valid_chart_type("2"))  # Valid chart type
        self.assertFalse(is_valid_chart_type("3")) # Invalid chart type
        self.assertFalse(is_valid_chart_type("a")) # Invalid chart type (non-numerical)
        self.assertFalse(is_valid_symbol(None)) # Invalid chart type (null)

    def test_valid_time_series(self):
        self.assertTrue(is_valid_time_series("1"))  # Valid time series
        self.assertTrue(is_valid_time_series("4"))  # Valid time series
        self.assertFalse(is_valid_time_series("5"))  # Invalid time series 
        self.assertFalse(is_valid_time_series("a"))  # Invalid time series (non-numerical)
        self.assertFalse(is_valid_time_series(None))  # Invalid time series (null)
    
    def test_valid_date(self):
        self.assertTrue(is_valid_date("2025-04-25"))  # Valid date
        self.assertFalse(is_valid_date("2025-04-31"))  # Invalid date (April 31st does not exist)
        self.assertFalse(is_valid_date("2025-13-25"))  # Invalid date (there is not 13 months)
        self.assertFalse(is_valid_date("2025-04-2"))  # Invalid date (day must be two numbers)
        self.assertFalse(is_valid_date("04-04-02"))  # Invalid date (year must be four number)
        self.assertFalse(is_valid_date("2025-4-02"))  # Invalid date (month must be two numbers)
        self.assertFalse(is_valid_date(None))  # Invalid date (null)
