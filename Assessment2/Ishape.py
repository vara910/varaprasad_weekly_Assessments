# •	16. Create an interface `IShape` with an abstract method `calculate_area()`. Implement it in `Rectangle` and `Circle` classes.
from abc import ABC,abstractmethod
class IShape(ABC):
    @abstractmethod
    def calculate_Area():
        pass
class Rectangle(IShape):
    def calculate_Area(self,len,width):
        return len*width
class Circle(IShape):
    def calculate_Area(self,radius):
        return 3.14*radius*radius
rect=Rectangle()
print(rect.calculate_Area(21,2))
circum=Circle()
print(circum.calculate_Area(2))
        
        