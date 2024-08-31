# 1. Person Class
class Person:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id_number}"
    

person1 = Person('Vera Wang', 45687)
print(person1)


instructor1 = Person("Angela Yu", 109809)
print(instructor1)