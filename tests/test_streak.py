import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_single_streak():
    assert longest_positive_streak([1, 1, 1]) == 3

def test_multiple_streaks():
    data = [2, 3, -1, 5, 6, 7, 0, 4]
    assert longest_positive_streak(data) == 3

def test_streaks_with_negatives_and_zeros():
    data = [0, -1, 2, 3, 0, 4, 5, 6, -2, 1]
    assert longest_positive_streak(data) == 3
