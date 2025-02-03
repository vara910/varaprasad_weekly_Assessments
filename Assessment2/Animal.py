# •	8. Design a system where a base class `Animal` has a method `speak()`, and subclasses `Dog` and `Cat` override it.
class Animal():
    def speak(self):
        print("all the animals can make different sounds")
class Dog(Animal):
    def speak(self):
      
        print("bark!")
        super().speak()
        
class Cat(Animal):
    def speak(self):
        print("meow!")

dog = Dog()
cat = Cat()

dog.speak()     
cat.speak()