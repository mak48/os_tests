import pytest
from functions_for_test import gcd, quick_exp


@pytest.mark.parametrize(
    ('num1', 'num2', 'res'), [
        (2, 4, 2),
        (512, 2304, 256),
        (3003, 18, 3),
    ]
)
def test_function_gcd(num1, num2, res):
    assert gcd(num1, num2) == res


@pytest.mark.parametrize(
    ('val', 'power', 'res'), [
        (3, 3, 27),
        (5, 10, 9765625),
        (36, 6, 2176782336),
    ]
)
def test_function_quick_exp(val, power, res):
    assert quick_exp(val, power) == res
