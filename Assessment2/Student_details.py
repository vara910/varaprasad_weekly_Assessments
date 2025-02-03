# •	4. Implement a `Student` class with a constructor that initializes `name` and `roll_number`. Write a method to return student details.
class Student():
    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number 
        
    def stu_details(self):
        return f"student name:{self.name}, student roll number:{self.roll_number}"
stu=Student("varaprasad",29)
print(stu.stu_details())