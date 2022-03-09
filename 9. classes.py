# Consider an example of declaring the examination result. Design three classes: Student, Exam, and Result.

# The Student class has data members such as those representing rollNumber, Name, etc. Create the class Exam by inheriting Student class.
class Student:
    def __init__(self, rollNumber, name, age):
        self.rollNumber = rollNumber
        self.name = name
        self.age = age

# The Exam class adds fields representing the marks scored in three subjects.
class Exam(Student):
    marks = {
        "Physics": 0,
        "Chemistry": 0,
        "Maths": 0,
    }
    def __init__(self, rollNumber, name, age, marks):
        super().__init__(rollNumber, name, age)
        self.marks = marks
# Derive Result from the Exam class, and it has its own fields such as total_marks.
class Result(Exam):
    def __init__(self, rollNumber, name, age, marks):
        super().__init__(rollNumber, name, age, marks)
        self.total_marks = sum(self.marks.values())
    def display(self):
        print("Roll Number:", self.rollNumber)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Marks:", self.marks)
        print("Total Marks:", self.total_marks)

# Write an interactive program to model this relationship.
if __name__ == "__main__":
    rollNumber = int(input("Enter Roll Number: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    marks = {
        "Physics": int(input("Enter Physics Marks: ")),
        "Chemistry": int(input("Enter Chemistry Marks: ")),
        "Maths": int(input("Enter Maths Marks: ")),
    }
    result = Result(rollNumber, name, age, marks)
    result.display()
