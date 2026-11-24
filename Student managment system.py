
class Student:
    def __init__(self, id, name, surname, email):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.courses = []

    def register_course(self, course):
        self.courses.append(course)
        print(self.name, "registered for", course.name)

    def drop_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            print("Course dropped")

    def view_grades(self):
        print("Student:", self.name)
        for course in self.courses:
            print(course.name, "Grade:", course.grade)


class Course:
    def __init__(self, id, name, credits):
        self.id = id
        self.name = name
        self.credits = credits
        self.grade = "Not assigned"


class Department:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def add_course(self, course):
        self.courses.append(course)


class Instructor:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def assign_grade(self, course, grade):
        course.grade = grade
        print("Grade assigned:", grade)

student1 = Student(20244150, "Mehmet", "Aygun", "mehmet@email.com")

course1 = Course(101, "Python", 3)

department1 = Department("Computer Science")

instructor1 = Instructor("John", "john@email.com")

department1.add_student(student1)
department1.add_course(course1)

student1.register_course(course1)

instructor1.assign_grade(course1, "A")

student1.view_grades()
