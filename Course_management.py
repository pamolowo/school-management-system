from Enrollment import Enrollment

# 6. Student Management System
class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.instructors = {}
        self.courses = {}
        self.enrollments = []

    # Student Management
    def add_student(self, student):
        self.students[student.id_number] = student

    def remove_student(self, id_number):
        if id_number in self.students:
            del self.students[id_number]

    def update_student(self, id_number, name=None, major=None):
        student = self.students.get(id_number)
        if student:
            if name:
                student.name = name
            if major:
                student.major = major

    # Instructor Management
    def add_instructor(self, instructor):
        self.instructors[instructor.id_number] = instructor

    def remove_instructor(self, id_number):
        if id_number in self.instructors:
            del self.instructors[id_number]

    def update_instructor(self, id_number, name=None, department=None):
        instructor = self.instructors.get(id_number)
        if instructor:
            if name:
                instructor.name = name
            if department:
                instructor.department = department

    # Course Management
    def add_course(self, course):
        self.courses[course.course_id] = course

    def remove_course(self, course_id):
        if course_id in self.courses:
            del self.courses[course_id]

    def update_course(self, course_id, course_name=None):
        course = self.courses.get(course_id)
        if course:
            if course_name:
                course.course_name = course_name

    # Enrollment 
    def enroll_student_in_course(self, student_id, course_id):
        student = self.students.get(student_id)
        course = self.courses.get(course_id)
        if student and course:
            course.add_student(student)
            enrollment = Enrollment(student, course)
            self.enrollments.append(enrollment)
            return enrollment
        return None

    def assign_grade(self, student_id, course_id, grade):
        for enrollment in self.enrollments:
            if enrollment.student.id_number == student_id and enrollment.course.course_id == course_id:
                enrollment.assign_grade(grade)
                return enrollment
        return None

    # get enrolled students in a course
    def get_students_in_course(self, course_id):
        course = self.courses.get(course_id)
        if course:
            return course.enrolled_students
        return []

    # get courses a student is enrolled In
    def get_courses_for_student(self, student_id):
        student_courses = []
        for enrollment in self.enrollments:
            if enrollment.student.id_number == student_id:
                student_courses.append(enrollment.course)
        return student_courses
