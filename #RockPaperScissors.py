#RockPaperScissors
#If choice is not valid print an error 
#Let the computer make a choice 
#print choices
#determine the winner 
#ask the user whether they want to continue
#if not stop the code 

import random

emojis = {"rock": "🪨", "paper": "📄", "scissors": "✂️"}
choices = ("rock", "paper", "scissors")

while True:

    user_choice = input("Enter rock, paper or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice.")
        continue

    computer_choice = random.choice(choices)

    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")

    else:
        print("Computer wins!")

    question = input("Play again? (y/n): ").lower()

    if question == "n":
        print("Thanks for playing!")
        break