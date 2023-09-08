
from student_code import Subject, InvalidStudentGrade, InvalidTestScore

def run_student_test():
    try:
        subject = Subject()
        subject.add_grade(5)
        subject.add_test_score(90)
        print("Grades:", subject.grades)
        print("Test Scores:", subject.test_scores)
        
        subject.add_grade(7)
    except InvalidStudentGrade as e:
        print("Exception caught:", e.message)

    try:
        subject.add_test_score(-10)
    except InvalidTestScore as e:
        print("Exception caught:", e.message)
