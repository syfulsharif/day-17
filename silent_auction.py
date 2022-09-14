import os
# HINT: You can call clear() to clear the output in the console

print("Welcome to the secret auction program")
bids = {}
next_bidder = True


def save_data():
    name = input("What is your name?\n")
    bids[name] = int(input("What is your bid: $"))


def highest_bidder(bids):
    highest_bid = 0
    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
            winner = bidder
    print(f"The winner is {winner} with highest ${highest_bid} bid.")


while next_bidder:
    save_data()
    next_bid = input("Are there any new bidder? Type: 'yes' or 'no'")
    if next_bid == "yes":
        os.system('clear')
        continue
    else:
        next_bidder = False
        highest_bidder(bids)

highest_bid = 0
print(bids)
