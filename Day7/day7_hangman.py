import random
import art

word_list = ["aardvark", "baboon", "camel"]
game = True
lives = 6

Chosen_Word = random.choice(word_list)
word_length = len(Chosen_Word)

display = []
for i in range(word_length):
    display.append("_")

while game == True:
    print(f"Lives = {lives}")
    Guess = input("Guess a letter: ").lower()


    for i in range(word_length):
        if Chosen_Word[i] == Guess:
            display[i] = Guess



    if Guess in Chosen_Word:
        print(display)
        print(art.stages[lives])

    elif Guess not in Chosen_Word:
        print(display)
        lives = lives - 1
        print(art.stages[lives])


    if "_" not in display:
        game = False
        print("You Win!")

    if lives == 0:
        print("You Lose!")
