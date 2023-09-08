# Импортируем нужные модули
import csv

# Дескриптор для проверки ФИО
class CapitalizedDescriptor:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not value.istitle() or not value.isalpha():
            raise ValueError("The name must start with a capital letter and contain only letters.")
        instance.__dict__[self.name] = value

# Класс предмета
class Subject:
    def __init__(self):
        self.grades = []
        self.test_scores = []

    def add_grade(self, grade):
        if grade < 2 or grade > 5:
            raise ValueError("Grade must be between 2 and 5.")
        self.grades.append(grade)

    def add_test_score(self, score):
        if score < 0 or score > 100:
            raise ValueError("Test score must be between 0 and 100.")
        self.test_scores.append(score)

    def average_test_score(self):
        return sum(self.test_scores) / len(self.test_scores) if self.test_scores else 0

# Основной класс студента
class Student:
    first_name = CapitalizedDescriptor("first_name")
    last_name = CapitalizedDescriptor("last_name")

    def __init__(self, first_name, last_name, subjects_file):
        self.first_name = first_name
        self.last_name = last_name
        self.load_subjects(subjects_file)

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Пропускаем заголовок
            self.subjects = {row[0]: Subject() for row in reader}

    def add_grade(self, subject, grade):
        if subject not in self.subjects:
            raise ValueError(f"Subject {subject} is not allowed.")
        self.subjects[subject].add_grade(grade)

    def add_test_score(self, subject, score):
        if subject not in self.subjects:
            raise ValueError(f"Subject {subject} is not allowed.")
        self.subjects[subject].add_test_score(score)

    def average_grade(self):
        all_grades = [grade for subject in self.subjects.values() for grade in subject.grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def average_test_score(self, subject):
        if subject not in self.subjects:
            raise ValueError(f"Subject {subject} is not allowed.")
        return self.subjects[subject].average_test_score()

# Создание экземпляра класса Student
student = Student("John", "Doe", "Seminar12\subjects.csv")

# Добавление оценок и результатов тестов
student.add_grade("Mathematics", 5)
student.add_grade("Physics", 4)
student.add_test_score("Mathematics", 90)
student.add_test_score("Physics", 85)

# Получение средних баллов
print(f"Average grade: {student.average_grade()}")
print(f"Average test score in Mathematics: {student.average_test_score('Mathematics')}")
