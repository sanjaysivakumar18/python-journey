import random
choices = ["rock", "paper", "scissors"]
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice>=3 or user_choice<0:
    print("You typed an invalid number, please reenter 0, 1 or 2.")
else:
    computer_choice=random.randint(0,2)

    print("You chose:",choices[user_choice])
    print("Computer chose:",choices[computer_choice])

    if user_choice == computer_choice:
        print("It's a Draw!")

    elif user_choice == 0 and computer_choice == 2:
        print("You Win!")

    elif user_choice == 1 and computer_choice == 0:
        print("You Win!")

    elif user_choice == 2 and computer_choice == 1:
        print("You Win!")
    
    else:
        print("Computer Wins")