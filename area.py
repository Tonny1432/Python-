class Shape():
    def display_info(self):
        print("THE AREA")

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def display_info(self):
         area_rectangle=self.length*self.width
         super().display_info()
         print("They area of the Rectangle  is:",area_rectangle)

class Square(Shape):
    def __init__(self,side):
        self.side=side
    def display_info(self):
         area_sqaure = self.side*self.side
         super().display_info()
         print("They area of the Sqaure is:",area_sqaure)

class Circle(Shape):
    def __init__(self,radius,):
        self.radius=radius

    def display_info(self):
         pi=3.14
         area_circle= pi*(self.radius**2)
         super().display_info()
         print("They area of the circle is:",area_circle)
        
class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def display_info(self):
        area_triangle= 0.5*(self.base*self.height)
        super().display_info()
        print("They area of the Triangle is:",area_triangle)


rectangle=Rectangle(25,30)
rectangle.display_info()
print("\n")
square=Square(30)
square.display_info()
print("\n")
circle=Circle(65)
circle.display_info()
print("\n")
triangle=Triangle(15,25)
triangle.display_info()



