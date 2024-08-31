from Main import Person

# 3. Instructor Class (inherits from Person)
class Instructor(Person):
    def __init__(self, name, id_number, department):
        super().__init__(name, id_number)
        self.department = department

    def __str__(self):
        return f"Instructor: {self.name}, ID: {self.id_number}, Department: {self.department}"


# Import Vera Wang's details (from the previously created Person object)
from Main import instructor1

# Create a Student object using Vera Wang's name and IDand ading a subject
new_instructor = Instructor(instructor1.name, instructor1.id_number, "Web Design")

# Output the student detailscreated
print(new_instructor)