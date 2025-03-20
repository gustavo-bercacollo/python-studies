

def analyzer_grades(* grades, student_status = False):
    """
    Analyze student grades and provide information about the performance.

    Parameters:
    grades (float): A series of student grades.
    student_status (bool): Whether to calculate the student's status based on their average.

    Returns:
    dict: A dictionary containing total grades, highest and lowest grades, average grade, and optionally the status.
    """
    student_data = {
        'total': len(grades),
        'largest': max(grades),
        'lowest': min(grades),
        'average': float(f'{sum(grades) / len(grades):.1f}')
    }

    if student_status:
        if student_data['average'] < 5:
            student_data['status'] = 'BAD'
        elif 7 > student_data['average'] >= 5:
            student_data['status'] = 'REASONABLE'
        else:
            student_data['status'] = 'GOOD'

    return student_data



user_enter = analyzer_grades(4, 7, 9, 3, 4, 5, 20, student_status=True)
print(user_enter)
