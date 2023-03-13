import random

attempts = 0
play = True
random_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print(f"Random number is {random_number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")


if difficulty == 'easy':
    attempts = 10

elif difficulty == 'hard':
    attempts = 5

while play == True and attempts != 0:
    print(f"You have {attempts} remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == random_number:
        print("You Win!. Congratulations")
        play = False

    elif guess > random_number:
        print("Too high.")
        print("Guess again.")
        attempts = attempts - 1

    elif guess < random_number:
        print("Too low.")
        print("Guess again.")
        attempts = attempts - 1

if attempts == 0:
    print("You have no right to try.")
