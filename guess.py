import random
def guess_no():
    c = 0
    secrete = random.randint(1, 100)
    i=0
    print("*" * 100)
    print("  Welcome to the Game of guessing Random Number")
    print("  You can guess a number between 1 - 100 ")
    for i in range(0,5):
        number = int(input("Enter the a number:"))
        if(number<=0):
            print("Zero or Negative  are consider as wrong input\nTry Again\nRestart the game")
            break
        if(number>secrete):
            print("The number is high")
            c+=1
            continue
        elif(number<secrete):
            print("The number is low")
            c+=1
            continue
        elif(number==secrete):
            print("You choose the correct answer\n--- YOU WIN ---")
            break
    print("*" * 100)
    if(c==5):
        print("you are not choose the correct number\n--- YOU LOST---\n The scecret number is:",secrete)
while True:
    guess_no()
    choice = input("Do you want to play again?\n(yes/no):").lower()
    if choice != 'yes':
        print("Thank you for playing \nGoodbye...")
        break