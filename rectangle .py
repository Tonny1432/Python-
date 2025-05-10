'''class Rectangle:
    def __init__(self,height,width):
        self.width=width
        self.height=height

    def area(self):
        print("The height is :",self.height)
        print("The width is:",self.width)
        Area=self.width*self.height
        print("The area of rectangle is:",Area)

    def perimeter(self):
        print("The height is :",self.height)
        print("The width is:",self.width)
        Perimeter=2*(self.width+self.height)
        print("The Perimeter of rectangle is:",Perimeter)

myrectangle=Rectangle(65,85)
myrectangle.area()
myrectangle.perimeter()'''


class Reactangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2*(self.width+self.height)
myrectangle=Reactangle(2,5)
print("width is",myrectangle.width)
print("height is",myrectangle.height)
print("area is",myrectangle.area())
print("perimeter is",myrectangle.perimeter())
