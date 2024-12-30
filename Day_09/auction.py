print("Welcome to the secret auction program!")

bidders = []  # List to store bidders and their bids
while True:
    bidder_name = input("Enter your name: ")
    bidders.append({"name": bidder_name, "bid": 0})  # Initialize bid for the user
    
    more = input("Are there any more bidders? Type 'yes' or 'no': ").lower()
    if more == "no":
        break

# Dictionary to keep track of the highest bid
max_bid = {"winner": "", "bid": 0}

while True:
    bidder_name = input("Who wants to bid? Type your name or 'no' if no one wants to bid: ").lower()
    if bidder_name == "no" or bidder_name == "nobody":
        break

    bid_amount = input("What's your bid? ")
    if not bid_amount.isdigit():
        print("Invalid input! Please enter a numeric value for the bid.")
        continue
    bid_amount = int(bid_amount)
    
    if bid_amount > max_bid["bid"]:
        max_bid["winner"] = bidder_name
        max_bid["bid"] = bid_amount
    else:
        print("Bid can't be lower than or equal to the current max bid.")

print(f"The winner is {max_bid['winner']} with a bid of {max_bid['bid']}.")
