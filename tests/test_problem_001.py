import pytest
from solutions.problem_001.multiples import sum_multiples_of_3_and_5

def test_project_euler_example():
    """Verify the baseline example provided by Project Euler (Limit = 10)."""
    assert sum_multiples_of_3_and_5(10) == 23

def test_project_euler_solution():
    """Verify the actual final solution for the benchmark (Limit = 1000)."""
    assert sum_multiples_of_3_and_5(1000) == 233168

def test_boundary_conditions():
    """Test lower boundary limits where no multiples should exist."""
    assert sum_multiples_of_3_and_5(0) == 0
    assert sum_multiples_of_3_and_5(3) == 0  # Below 3 means 3 is excluded
    assert sum_multiples_of_3_and_5(4) == 3  # Only 3 is included

def test_negative_limit_exception():
    """Ensure the system tightly rejects invalid inputs by throwing a ValueError."""
    with pytest.raises(ValueError, match="Limit must be a positive integer."):
        sum_multiples_of_3_and_5(-10)