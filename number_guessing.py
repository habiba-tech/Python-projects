import random
number_to_guess = random.randint(1,100)

while True :
    try:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess < number_to_guess:
            print("To low!!")
        elif guess > number_to_guess:
            print("To high!")
        else:
            print("Conguratulation! You guessed the number. ")
            break
    except ValueError :
        print("Please enter a valid numbeer ")
