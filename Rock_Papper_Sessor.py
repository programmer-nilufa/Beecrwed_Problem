import random
user_Choice = int(input("0 is rock. \n1 is paper. \n2 is sessor. \nEnter Here:"))
computer_Choice = random.randint(0,2)
print("Computer Choice:")
print(computer_Choice)
if user_Choice > computer_Choice :
    print("You Win")
elif computer_Choice > user_Choice :
    print("You loss")
elif computer_Choice == user_Choice :
    print("Draw the game")
