import random

lowest_num = 1
higest_num = 50

answer = random.randint(lowest_num, higest_num)
 
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {higest_num}")


while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess<lowest_num or guess>higest_num:
            print("That number is out of range")
            print(f"Please Select a number between {lowest_num} and {higest_num}")
        elif guess<answer:
            print("Too low! Try again!")
        elif guess>answer:
            print("Too high! Try again!")    
        else:
            print(f"CORRECT! The aanswer was {answer}")
            print(f"Number of guess: {guesses}")
            is_running = False

    else:
        print("Invalid guess")
        print(f"Please Select a number between {lowest_num} and {higest_num}")


