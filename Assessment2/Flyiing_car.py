class Car:
    def move(self):
        print("The car drives on the road.")

class Airplane:
    def move(self):
        print("The airplane flies in the sky.")

class FlyingCar(Car, Airplane): 
    def move(self):
        print("The flying car can both drive and fly!")
        Car.move(self)     
        Airplane.move(self)  
fc = FlyingCar()
fc.move()
