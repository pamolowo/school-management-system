from Main import Person


# 2. Student Class(inherits from Person)
class Student(Person):
    def __init__(self, name, id_number, major):
        super().__init__(name, id_number) #using super() toinherit
        self.major = major

    def __str__(self):
        return f"Student: {self.name}, ID: {self.id_number}, Major: {self.major}"


# Import Vera Wang's details (from the previously created Person object)
from Main import person1

# Create a Student object using Vera Wang's name and IDand ading a subject
student1 = Student(person1.name, person1.id_number, "Fashion Design")

# Output the student detailscreated
print(student1)