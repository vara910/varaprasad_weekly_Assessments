# •	7. Create a multi-level class structure with `Person` → `Employee` → `Manager`, where `Manager` has an additional method `approve_leave()`.
class Person():
    def __init__(self):
        pass
    def person_details():
        pass
    def disp():
        pass
class Employee(Person):
    def person_details(self,name,gender,role):
        self.name=name
        self.gender=gender
        self.role=role
    def disp(self):
        return f"employee_name:{self.name}\nsex:{self.gender}\ndesignation:{self.role}"
    
class Manager(Person):
         def person_details(self):
            pass
         def disp():
             pass
         def approve_leave(self,name):
             self.name=name
             return f"{self.name} your leave has been approved"
cla=Employee()
cla.person_details("vara","male","developer")
print(cla.disp())
mla=Manager()
mla.approve_leave("vara")
print(mla.approve_leave("vara"))
             
        