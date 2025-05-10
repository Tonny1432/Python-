import math
print("Hello guys this is my calacuator")
print ("Can you select any option below")
print("\n1.addation\n2.substration\n3.multiplaction\n4.division\n5.exponential\n6.square root")
option=int(input("Enter your option:"))
if(option==1):
    class adder:
        def add(self):
            a=int(input("enter the number:"))
            b=int(input("enter the number:")) 
            c=a+b
            print("print the addtations of two number is:",c)
    additation=adder()
    additation.add()
elif(option==2):
    class subract:
        def sub(self):
            a=int(input("enter the number:"))
            b=int(input("enter the number:")) 
            c=a-b
            print("print the substratin of two number is:",c)
    substration=subract()
    substration.sub()
elif(option==3):
    class multipler:
        def mult(self):
            a=int(input("enter the number:"))
            b=int(input("enter the number:")) 
            c=a*b
            print("print the multiplacation of two number is:",c)
    multiplication=multipler()
    multiplication.mult()
elif(option==4):
    class divider:
       def div(self):
           a=int(input("enter the number:"))
           b=int(input("enter the number:")) 
           if(b==0):
               print("The divider cannot be zero")
           else:
             c=a/b
             print("print the division of two number is:",c)
    division=divider()
    division.div()
elif(option==5):
    class expotential:
        def expo(self):
            a=int(input("enter the number:"))
            b=int(input("enter the number:")) 
            c=a**b
            print("print the expontential of  number is:",c)
    Expotential=expotential()
    Expotential.expo()
elif(option==6):
    class square_root:
        def sqrt(self):
            a=int(input("enter the number:"))
            c=math.sqrt(a)
            print("print the square root of two number is:",c)
    squareroot=square_root()
    squareroot.sqrt()
else:
    print("you choose wrong option")





