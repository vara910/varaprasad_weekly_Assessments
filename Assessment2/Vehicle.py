# •	6. Implement a multi-level inheritance example where `Vehicle` is a base class, `Car` and `Bike` inherit from `Vehicle`, and `ElectricCar` inherits from `Car`.
class Vehicle():
    def __init__(self):
        pass
    def run():
      pass
class Bike(Vehicle):
    def __init__(self,two_wheeler):
        super().__init__()
        self.two_wheeler=two_wheeler
    def run(self):
        return f"{self.two_wheeler} has two wheels and runs on only petrol"
class Car(Vehicle):
    def __init__(self,four_wheeler):
        super().__init__()
        self.four_wheeler=four_wheeler
    def run(self):
        return f"{self.four_wheeler} has four wheels and runs on both diesel and petrol"
class Electric(Car):
    def __init__(self, four_wheeler):
        super().__init__(four_wheeler)
    def run(self):
        return f"{self.four_wheeler} has four wheels and runs on electricity"

bk=Bike("honda bike")
ck=Car("maruti car")
mg=Electric("MG Hector")
print(bk.run())
print(ck.run())
print(mg.run())
