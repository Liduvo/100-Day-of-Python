import art

print(art.logo)

secret_auction = True
auction_dict = {}

def controller(dict):
    winner = ""
    best_price = 0

    for key, value in auction_dict.items():

        if value > best_price:
            best_price = value
            winner = key


    print(f"The winner is {winner} with a bid of ${best_price}")


while secret_auction == True:
    name = input("What is your name?: ")
    price = float(input("Enter price $"))

    auction_dict.update({name: price})

    yes_no = input("Are they any other bidders? Type 'yes' or 'no'. ")

    if yes_no == "yes":
        secret_auction == True

    elif yes_no == "no":
        controller(auction_dict)
        secret_auction == False

    else:
        print("Please 'yes or 'no' ")
