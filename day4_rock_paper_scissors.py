import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

print("Welcome the rock Paper Scissors")
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
if player_choice in [0 ,1 ,2]:
    print(game_images[player_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice}")
print(game_images[computer_choice])

if player_choice not in [0, 1, 2]:
    print("You typed an invalid number, you lose!")
elif player_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and player_choice == 2:
    print("You lose")
elif computer_choice > player_choice:
    print("You lose")
elif player_choice > computer_choice:
    print("You win!")
elif player_choice == computer_choice:
    print("It's a draw")
    
