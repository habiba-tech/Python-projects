import random

while True:
    choice = input("Roll a dice? (Yes/No): ")

    if choice.lower() == "yes":
        try:
            option = int(input("How many dice do you want to roll (e.g., 3 or 5)? "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if option == 3:
            dice = [random.randint(1, 6)for _ in range(3)]
            print(f"You rolled: {dice}")
        elif option == 5:
            dice = [random.randint(1, 6) for _ in range(5)]
            print(f"You rolled: {dice}")
        else:
            print("Only 3 or 5 dice can be rolled.")
    elif choice.lower() == "no":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice. Please enter Yes or No.")
