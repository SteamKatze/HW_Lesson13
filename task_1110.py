class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    @staticmethod
    def description():
        print("This is a general person")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def show_info(self):
        super().show_info()
        print(f"Student ID: {self.student_id}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def show_info(self):
        super().show_info()
        print(f"Teaches: {self.subject}")


class Subject:
    def __init__(self, name):
        self.name = name


class Course:
    def __init__(self, title, subject, teacher):
        self.title = title
        self.subject = subject
        self.teacher = teacher


class Department:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def add_course(self, course):
        if isinstance(course, Course):
            self.courses.append(course)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        for book in self.books:
            print(book)


class Administration:
    def __init__(self):
        self.staff = []

    def add_staff(self, person):
        if isinstance(person, Person):
            self.staff.append(person)


class Academy:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
        self.subjects = []
        self.departments = []
        self.library = Library()
        self.administration = Administration()

    def add_teacher(self, teacher):
        if isinstance(teacher, Teacher):
            self.teachers.append(teacher)

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)

    def add_subject(self, subject):
        if isinstance(subject, Subject):
            self.subjects.append(subject)

    def add_department(self, department):
        if isinstance(department, Department):
            self.departments.append(department)


print(Student.mro())