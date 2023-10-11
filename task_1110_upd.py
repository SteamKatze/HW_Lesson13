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


class Academy:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
        self.subjects = []
        self.departments = []

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

    def show_info(self):
        print(f"Academy Name: {self.name}")
        print("\nTeachers:")
        for teacher in self.teachers:
            teacher.show_info()
        print("\nStudents:")
        for student in self.students:
            student.show_info()
        print("\nSubjects:")
        for subject in self.subjects:
            print(subject.name)
        print("\nDepartments:")
        for department in self.departments:
            print(department.name)

print(Student.mro())

# Test

spy_subject = Subject("Hand to hand combat")
MrSmith_teacher = Teacher("Mr Smith", 35, spy_subject.name)
MrsSmith_student = Student("Mrs Smith", 20, "A007")
spy_course = Course("Spy, Group 101", spy_subject, MrSmith_teacher)
spy_dept = Department("CIA")
spy_dept.add_course(spy_course)

academy = Academy("Spy Academy")
academy.add_teacher(MrSmith_teacher)
academy.add_student(MrsSmith_student)
academy.add_subject(spy_subject)
academy.add_department(spy_dept)

academy.show_info()