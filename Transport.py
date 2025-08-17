#In OOP, Inheritance means one class (child class) can reuse the attributes and methods of another class (parent class).
class vechicle:# parent class
    def __init__(self,Brand,Model,Year):         # init__ is a constructor in Python classes.
        self.Brand=Brand                         #It runs automatically when an object is created.
        self.Model=Model                         #It is used to initialize attributes of the object.
        self.Year=Year                           #The first parameter is always self (represents the current object).
    def display_details(self):                   
        print("They Model is:",self.Model)
        print("They brand is:",self.Brand)                                    
        print("They year is:",self.Year) 
class Car(vechicle):# Car child class 
    def __init__(self, Brand, Model, Year,Type):
        super().__init__(Brand, Model, Year)         #super() is used inside a child class to call methods of the parent class
        self.Type=Type                               #Commonly used in __init__ to avoid rewriting parent’s initialization code.
    def display_details(self):
        super().display_details()
        print("They type of the car is:",self.Type)
class Bike(vechicle):# Bike child class
    def __init__(self, Brand, Model, Year,Type):
        super().__init__(Brand, Model, Year)
        self.Type=Type
    def display_details(self):
        super().display_details()
        print("They type of the car is:",self.Type)
class Bus(vechicle):
    def __init__(self, Brand, Model, Year,passenger_capacity):
        super().__init__(Brand, Model, Year)
        self.passenger_capacity=passenger_capacity
    def display_details(self):
        super().display_details()
        print("They the passenger they can hold it:",self.passenger_capacity)
class Truck(vechicle):
    def __init__(self, Brand, Model, Year,Weight_capacity):
        super().__init__(Brand, Model, Year)
        self.Weigth_capcity=Weight_capacity
    def display_details(self):
        super().display_details()
        print("The weight cpacity of the turck is:",self.Weigth_capcity)
car=Car("Toyota","Corolla",2020,"Sedan")
bike=Bike("Yamaha","R15",2020,"Sport bike")
bus=Bus("Tata","Star bus ultra",2020,45)
truck=Truck("Tata","LPT 4018",2020,"100kg")
car.display_details()
print("\n")
bike.display_details()
print("\n")
bus.display_details()
print("\n")
truck.display_details()
