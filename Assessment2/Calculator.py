from abc import ABC,abstractmethod
class Calculator(ABC):
    @abstractmethod
    def add(self):
        print("this is for addition")
    @abstractmethod
    def sub(self):
         print("this is for substraction")
    @abstractmethod
    def mul(self):
        print("this is for multiplication")
    @abstractmethod
    def div(self):
        print("this is for division")
class Calculation(Calculator):
    def add(self,num1,num2):
        super().add()
        return num1+num2
    def sub(self,num1,num2):
        super().sub()
        return num1-num2 
    def mul(self,num1,num2):
        super().mul()
        return num1*num2
    def div(self,num1,num2):
        super().div()
        return num1/num2       
calc=Calculation()
print(calc.add(2,4))
print(calc.sub(22,4))
print(calc.mul(2,4))
print(calc.div(200,4))




        