import random

choices = ["rock", "paper", "scissors"]

while True:
    user = input("Rock, Paper, Scissors? (or quit): ").lower()
    if user == "quit":
        print("Goodbye!")
        break
    if user not in choices:
        print("Invalid choice, try again.")
        continue

    comp = random.choice(choices)
    print(f"Computer chose: {comp}")

    if user == comp:
        print("It's a tie!")
    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        print("You win!")
    else:
        print("You lose!")
   