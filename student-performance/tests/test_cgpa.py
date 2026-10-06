import pytest

from src.cgpa import (
    calculate_cgpa,
    calculate_percentage,
    get_performance_category,
)

def test_calculate_cgpa():
    assert calculate_cgpa([8, 9, 7, 10]) == 8.5


def test_single_grade_point():
    assert calculate_cgpa([8]) == 8


def test_cgpa_boundary_values():
    assert calculate_cgpa([0, 10]) == 5


def test_empty_grade_points():
    with pytest.raises(ValueError):
        calculate_cgpa([])


def test_invalid_grade_point():
    with pytest.raises(ValueError):
        calculate_cgpa([8, 11])


def test_percentage():
    assert calculate_percentage(8.5) == 80.75


def test_invalid_cgpa():
    with pytest.raises(ValueError):
        calculate_percentage(11)

def test_performance_category():
    assert get_performance_category(9.2) == "Excellent"
    assert get_performance_category(8.5) == "Very Good"
    assert get_performance_category(7.5) == "Good"
    assert get_performance_category(6.5) == "Average"
    assert get_performance_category(5.5) == "Needs Improvement"