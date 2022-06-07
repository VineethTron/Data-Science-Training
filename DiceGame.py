
#DICE GAME

import random
while True:
    user_input = int(input("Enter a number between 1 & 6 : "))
    choices = [1, 2, 3, 4, 5, 6] #user input of dice
    ci = random.choice(choices) #computer choice
    print("Computer's choice = ",ci)
    if user_input > ci :
        print("You Won !! Game Over")
    elif user_input < ci :
        print("Computer Won!! Game Over")
    else:
        continue