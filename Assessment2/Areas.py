class Shape():
    def area(self):
        pass
class Square(Shape):
    def area(self,side):
        return side*side
class Triangle(Shape):
    def area(self,base,height):
        return base*height*0.5
cld=Square()
print("area of square:",cld.area(10))       
cd=Triangle()
print("area of triangle:",cd.area(10,2))       