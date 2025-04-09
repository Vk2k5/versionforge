import pytest
from features.score_calculator import compute_average_score
def test_compute_average_with_negative_numbers():
    """Test computing the average of scores including negative numbers."""
    scores = [90, -10, 80, -5]
    assert compute_average_score(scores) == (90 - 10 + 80 - 5) / 4
