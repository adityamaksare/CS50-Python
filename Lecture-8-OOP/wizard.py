class wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

# Student is a sub-class of wizard
class Student(wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

# Professor is a sub-class of wizard
class Professor(wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject


Wizard = wizard("Albus")
student = Student("Harry", "Gryffindor")
professor =  Professor("Severus",  "Defence Against Dark Arts")

