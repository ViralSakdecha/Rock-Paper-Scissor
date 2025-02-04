import random

print("Rock Paper Scissor")

print("Winning rules of the game are:\n" 
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

while True:

    try:
        print("Enter 1 for Rock\nEnter 2 for Paper\nEnter 3 for Scissor")
        choice = int(input())    
        if choice not in [1,2,3]:
            print("Enter number between 1 and 3:")
            continue

    except ValueError:
        print("Enter a number:")
        continue

    if choice==1:
            choice_name = "Rock"
    elif choice==2:
            choice_name = "Paper"
    elif choice==3:
            choice_name = "Scissor"

    print("Your choice:",choice_name,"\n")

    choice_computer = random.randint(1,3)

    if choice_computer==1:
        choice_computer_name = "Rock"
    elif choice_computer==2:
        choice_computer_name = "Paper"
    elif choice_computer==3:
        choice_computer_name = "Scissor"

    print("Computers choice:",choice_computer_name,"\n")

    if choice==choice_computer:
        result = "Draw"
    elif (choice==1 and choice_computer==2) or (choice_computer==1 and choice==2):
        result="Paper"
    elif (choice==1 and choice_computer==3) or (choice_computer==1 and choice==3):
        result="Rock"
    elif (choice==2 and choice_computer==3) or (choice_computer==2 and choice==3):
        result="Scissor"
    
    if result=="Draw":
        print("Draw!","\n")
    elif result==choice_name:
        print("User Wins!","\n")
    elif result==choice_computer_name:
        print("Computer Wins","\n")

    again=input("Do you want to play again? (Y/N)\n")
    

    if again=="n" or again=="N":
        break

print("Thanks for playing!")