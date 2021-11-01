from math_series import __version__
from math_series.series import lucas
from math_series.series import fibonacci
from math_series.series import sum_series

def test_version():
    assert __version__ == '0.1.0'


def test_fibonacci_7():
    excepted = 13
    actual = fibonacci(7)
    assert excepted == actual
def test_lucas_7():
    excepted = 29
    actual = lucas(7)
    assert excepted == actual

def test_sum_series_7():
    excepted = 13
    actual = sum_series(7)
    assert excepted == actual
