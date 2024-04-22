import pytest
from course_grader import convert_to_letter_grade

# TODO-1: Add test_exact_grade_boundaries() function
def test_exact_grade_boundaries():
    assert convert_to_letter_grade(0) == 'F'
    assert convert_to_letter_grade(39) == 'F'
    assert convert_to_letter_grade(64) == 'D'
    assert convert_to_letter_grade(71) == 'C'
    assert convert_to_letter_grade(79) == 'C'
    assert convert_to_letter_grade(80) == 'B'
    assert convert_to_letter_grade(89) == 'B'
    assert convert_to_letter_grade(90) == 'A'
    assert convert_to_letter_grade(100) == 'A'

# TODO-2: Add test_invalid_numerical_score() function
def test_invalid_numerical_score():
    with pytest.raises(ValueError, match = "Score must be between 0 and 100."):
        convert_to_letter_grade(105)
        convert_to_letter_grade(-5)

# TODO-3: Add test_non_numeric_input() function
def test_non_numeric_input():
    with pytest.raises(TypeError, match=r"Score must be a numeric value."):
        convert_to_letter_grade("90")
        convert_to_letter_grade([90])
        convert_to_letter_grade(None)
