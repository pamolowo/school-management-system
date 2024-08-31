# 5. Enrollment Class
class Enrollment:
    def __init__(self, student, course):
        self.student = student
        self.course = course
        self.grade = None

    def assign_grade(self, grade):
        self.grade = grade

    def __str__(self):
        grade_str = self.grade if self.grade is not None else "No grade assigned"
        return f"{self.student.name} enrolled in {self.course.course_name}, Grade: {grade_str}"