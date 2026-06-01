import pytest
from solutions.problem_002.fibonacci import sum_even_fibonacci

def test_fibonacci_small_limit():
    """Verify sequence up to 10: 1, 2, 3, 5, 8 (Evens are 2 and 8)."""
    assert sum_even_fibonacci(10) == 10

def test_fibonacci_boundary():
    assert sum_even_fibonacci(0) == 0
    assert sum_even_fibonacci(1) == 0

def test_negative_input():
    with pytest.raises(ValueError):
        sum_even_fibonacci(-500)