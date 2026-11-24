
class Student:
    def __init__(self, student_id, name, surname, email):
        self.student_id = student_id
        self.name = name
        self.surname = surname
        self.email = email
        self.enrollments = []

    def register_course(self, course):
        enrollment = Enrollment(self, course)
        self.enrollments.append(enrollment)
        course.enrollments.append(enrollment)
        print(f"{self.name} registered for {course.course_name}")

    def drop_course(self, course):
        for enrollment in self.enrollments:
            if enrollment.course == course:
                self.enrollments.remove(enrollment)
                course.enrollments.remove(enrollment)
                print(f"{course.course_name} dropped")
                return
        print("Enrollment not found")

    def view_grades(self):
        for enrollment in self.enrollments:
            print(enrollment.course.course_name, "Grade:", enrollment.grade)


class Course:
    def __init__(self, course_id, course_name, credits):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits
        self.enrollments = []

    def get_course_details(self):
        print(self.course_name, "Credits:", self.credits)


class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.enrollment_date = "2026-11-24"
        self.grade = "Not assigned"

    def assign_grade(self, grade):
        self.grade = grade
        print("Grade assigned:", grade)


class Department:
    def __init__(self, department_id, department_name):
        self.department_id = department_id
        self.department_name = department_name
        self.students = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        self.students.remove(student)


class Instructor:
    def __init__(self, instructor_id, name, email):
        self.instructor_id = instructor_id
        self.name = name
        self.email = email
        self.courses = []

    def teach_course(self, course):
        self.courses.append(course)
        print(self.name, "teaches", course.course_name)

    def assign_grade(self, enrollment, grade):
        enrollment.assign_grade(grade)

