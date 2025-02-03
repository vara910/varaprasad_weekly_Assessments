# •	1. Create a class `Employee` with properties `name`, `id`, and `department`. Instantiate an object and assign values dynamically.

class Employee():
    def __init__(self):
        self.name=None
        self.id=None
        self.department=None
        
    def emp_details(self):
        self.name=input("enter the name:")
        self.id=int(input("enter the id:"))
        self.department=input("enter the department:")
        
    def display(self):
        return f"name:{self.name}\nid:{self.id}\ndept:{self.department}\n"
emp=Employee()

emp.emp_details()
print(emp.display())
