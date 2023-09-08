
import csv

class InvalidStudentGrade(Exception):
    def __init__(self, grade):
        self.message = f"Invalid grade: {grade}. Grade should be between 2 and 5."
        super().__init__(self.message)

class InvalidTestScore(Exception):
    def __init__(self, score):
        self.message = f"Invalid test score: {score}. Test score should be between 0 and 100."
        super().__init__(self.message)

class Subject:
    def __init__(self):
        self.grades = []
        self.test_scores = []

    def add_grade(self, grade):
        if grade < 2 or grade > 5:
            raise InvalidStudentGrade(grade)
        self.grades.append(grade)

    def add_test_score(self, score):
        if score < 0 or score > 100:
            raise InvalidTestScore(score)
        self.test_scores.append(score)

    def average_test_score(self):
        return sum(self.test_scores) / len(self.test_scores) if self.test_scores else 0

class InvalidStudentGrade(Exception):
    def __init__(self, grade):
        self.message = f"Invalid grade: {grade}. Grade should be between 2 and 5."
        super().__init__(self.message)

class InvalidTestScore(Exception):
    def __init__(self, score):
        self.message = f"Invalid test score: {score}. Test score should be between 0 and 100."
        super().__init__(self.message)

class SubjectWithExceptions(Subject):  # Наследуемся от предыдущего класса Subject
    def add_grade(self, grade):
        if grade < 2 or grade > 5:
            raise InvalidStudentGrade(grade)
        super().add_grade(grade)

    def add_test_score(self, score):
        if score < 0 or score > 100:
            raise InvalidTestScore(score)
        super().add_test_score(score)