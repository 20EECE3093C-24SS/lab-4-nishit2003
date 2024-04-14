import pytest
from course_grader import convert_to_letter_grade

# TODO-1: Add test_exact_grade_boundaries() function
def test_exact_grade_boundaries():
    """
    Test function to verify the behavior of convert_to_letter_grade function
    at the exact grade boundaries.

    This function tests the behavior of the convert_to_letter_grade function
    at the precise score boundaries for each letter grade, ensuring that the
    correct letter grade is returned for each boundary score.

    Returns:
        None
    """
    assert convert_to_letter_grade(0) == 'F'
    assert convert_to_letter_grade(39) == 'F'
    assert convert_to_letter_grade(64) == 'D'
    assert convert_to_letter_grade(71) == 'D'
    assert convert_to_letter_grade(79) == 'C'
    assert convert_to_letter_grade(80) == 'B'
    assert convert_to_letter_grade(89) == 'B'
    assert convert_to_letter_grade(90) == 'A'
    assert convert_to_letter_grade(100) == 'A'

# TODO-2: Add test_invalid_numerical_score() function
def test_invalid_numerical_score():
    """
    Test function to verify that convert_to_letter_grade function raises a ValueError
    when provided with scores outside the permissible range of 0 to 100.

    This function tests the behavior of the convert_to_letter_grade function
    when given scores that are outside the valid range, ensuring that a ValueError
    is raised with the appropriate error message.

    Returns:
        None
    """
    with pytest.raises(ValueError) as exc_info:
        convert_to_letter_grade(105)
    assert str(exc_info.value) == "Score must be between 0 and 100."

    with pytest.raises(ValueError) as exc_info:
        convert_to_letter_grade(-5)
    assert str(exc_info.value) == "Score must be between 0 and 100."

# TODO-3: Add test_non_numeric_input() function
def test_non_numeric_input():
    """
    Test function to verify that convert_to_letter_grade function raises a TypeError
    when provided with non-numeric inputs.

    This function tests the behavior of the convert_to_letter_grade function
    when given inputs that are not valid numerical values, ensuring that a TypeError
    is raised with the appropriate error message.

    Returns:
        None
    """
    with pytest.raises(TypeError) as exc_info:
        convert_to_letter_grade("90")
    assert str(exc_info.value) == "Score must be a numeric value."

    with pytest.raises(TypeError) as exc_info:
        convert_to_letter_grade([90])
    assert str(exc_info.value) == "Score must be a numeric value."

    with pytest.raises(TypeError) as exc_info:
        convert_to_letter_grade(None)
    assert str(exc_info.value) == "Score must be a numeric value."
