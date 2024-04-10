# TODO-1: add convert_to_letter_grade(score) function

def convert_to_letter_grade(score):
   """
    Converts a student's numerical score into a corresponding letter grade.

    Args:
        score (int or float): The student's numerical score to be converted into a letter grade.

    Returns:
        str: An upper-case string indicating the student's letter grade.

    Raises:
        ValueError: If the input score is outside the range of 0 to 100.
        TypeError: If the input score is not an int or float.
    """
   
    # Check if the input score is a numeric value
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a numeric value.")

    # Check if the input score is within the range of 0 to 100
    if score < 0 or score > 100:
         raise ValueError("Invalid input. Please enter a number between 0 and 100.")

    # Convert score to letter grade based on predefined ranges
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

    
