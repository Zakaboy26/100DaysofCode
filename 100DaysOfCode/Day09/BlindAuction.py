import art
print(art.logo)

bidder = input("What is your name?:\n")
price = int(input("What is your bid?:\n$"))

bid_dictionary = {}
bid_dictionary[bidder] = (price)

def compare_bids():
    highest_bid = 0
    winner = ""
    for bidder in bid_dictionary:
        if bid_dictionary[bidder] > highest_bid:
            winner = bidder
            highest_bid = bid_dictionary[bidder]
    print(f"The max bidder is: {winner} with a bid of {highest_bid} ")

bid_again = True

while bid_again:
    another_bid = input("Want to add another bidder? (Y/N):\n").upper()
    if another_bid == "Y":
        bidder = input("What is your name?:\n")
        price = int(input("What is your bid?:\n$"))
        bid_dictionary[bidder] = (price)
    else:
        bid_again = False
        compare_bids()
