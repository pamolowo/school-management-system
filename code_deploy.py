from Main import Person
from Student import Student
from Instructor import Instructor
from Course import Course
from Enrollment import Enrollment
from Course_management import StudentManagementSystem



# Initialize the Student Management System
sms = StudentManagementSystem()

# Add Students
student1 = Student("Charlie Brown", 103, "Culinary Arts")
student2 = Student("Daisy Miller", 104, "Graphic Design")
student3 = Student("Alice Johnson", 101, "Carpentry")
student4 = Student("Bob Lee", 102, "Fashion Design")

sms.add_student(student1)
sms.add_student(student2)
sms.add_student(student3)
sms.add_student(student4)

# Add Instructors
instructor1 = Instructor("Chef Ramsey", 203, "Culinary Arts")
instructor2 = Instructor("Ms. Adams", 204, "Graphic Design")
instructor3 = Instructor("Ms. Green", 201, "Carpentry")
instructor4 = Instructor("Mr. White", 202, "Fashion Design")

sms.add_instructor(instructor1)
sms.add_instructor(instructor2)
sms.add_instructor(instructor3)
sms.add_instructor(instructor4)

# Add Courses
course1 = Course("Gourmet Cooking", "CUL101")
course2 = Course("Digital Illustration", "GRD201")
course3 = Course("Basic Carpentry", "CARP101")
course4 = Course("Advanced Fashion Design", "FASH201")

sms.add_course(course1)
sms.add_course(course2)
sms.add_course(course3)
sms.add_course(course4)

# enroll students in courses
enrollment1 = sms.enroll_student_in_course(103, "CUL101")
enrollment2 = sms.enroll_student_in_course(104, "GRD201")
enrollment3 = sms.enroll_student_in_course(101, "CARP101")
enrollment4 = sms.enroll_student_in_course(102, "FASH201")

# assign grades
sms.assign_grade(103, "CUL101", "A")
sms.assign_grade(104, "GRD201", "B+")
sms.assign_grade(101, "CARP101", "A-")
sms.assign_grade(102, "FASH201", "B")

# Get students in a course
print("Students in CUL101 - Gourmet Cooking:")
students_in_course = sms.get_students_in_course("CUL101")
for student in students_in_course:
    print(student)

print("\nStudents in CARP101 - Basic Carpentry:")
students_in_course = sms.get_students_in_course("CARP101")
for student in students_in_course:
    print(student)

# Get courses a student is enrolled in
print("\nCourses for Charlie Brown (ID: 103):")
courses_for_student = sms.get_courses_for_student(103)
for course in courses_for_student:
    print(course)

print("\nCourses for Alice Johnson (ID: 101):")
courses_for_student = sms.get_courses_for_student(101)
for course in courses_for_student:
    print(course)


