import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
random_list = []
password = ""

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
for i in range(nr_letters):
    random_letter = random.choice(letters)
    random_list.append(random_letter)

nr_symbols = int(input(f"How many symbols would you like?\n"))
for i in range(nr_symbols):
    random_symbols = random.choice(symbols)
    random_list.append(random_symbols)

nr_numbers = int(input(f"How many numbers would you like?\n"))
for i in range(nr_numbers):
    random_numbers = random.choice(numbers)
    random_list.append(random_numbers)

length_password = nr_letters + nr_symbols + nr_numbers
for i in range(length_password):
    all_random = random.choice(random_list)
    password = password + all_random

print(f"Your password is {password}")
