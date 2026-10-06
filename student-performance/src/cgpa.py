def calculate_cgpa(grade_points):
    """Calculate CGPA from grade points."""

    if not grade_points:
        raise ValueError("Grade points cannot be empty.")

    if any(point < 0 or point > 10 for point in grade_points):
        raise ValueError("Grade points must be between 0 and 10.")

    return round(sum(grade_points) / len(grade_points), 2)


def calculate_percentage(cgpa):
    """Convert CGPA to percentage."""

    if not 0 <= cgpa <= 10:
        raise ValueError("CGPA must be between 0 and 10.")

    return round(cgpa * 9.5, 2)


def get_performance_category(cgpa):
    """Return performance category based on CGPA."""

    if not 0 <= cgpa <= 10:
        raise ValueError("CGPA must be between 0 and 10.")

    if cgpa >= 9:
        return "Excellent"
    if cgpa >= 8:
        return "Very Good"
    if cgpa >= 7:
        return "Good"
    if cgpa >= 6:
        return "Average"

    return "Needs Improvement"