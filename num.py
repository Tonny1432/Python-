def nummber():
    print(
        "hello guy's  did u hear about the Geometric Progression pattern\n" 
        "   if u enter the two numbers u can see the pattern"
    )


number_1 = int(input(" enter the first number:"))
number_2 = int(input(" enter the second number:"))
i = 0
numb = 0
n = 50
number_3 = number_1 + number_2
print(number_1)
print(number_2)
print(number_3)
while i < n:
    numb = number_3 * 2
    print(numb)
    number_3 = numb
    i += 1
nummber()
