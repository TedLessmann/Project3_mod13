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