from resources import resources, latte, espresso, cappuccino

data = resources

# Keys for resources
water = "water"
milk = "milk"
coffee = "coffee"
money = "money"

def report():
    print("\nRemaining Resources:")
    print(f"Water: {data[water]}ml")
    print(f"Milk: {data[milk]}ml")
    print(f"Coffee: {data[coffee]}g")
    print(f"Money: ${data[money]}\n")

def check_resources(bev):
    """Checks if there are enough resources to make the beverage."""
    if (data[water] - bev[water] < 0):
        print("Sorry, not enough water.")
        return False
    if (data[milk] - bev[milk] < 0):
        print("Sorry, not enough milk.")
        return False
    if (data[coffee] - bev[coffee] < 0):
        print("Sorry, not enough coffee.")
        return False
    return True

def deduct(bev):
    """Deducts resources used for a beverage."""
    data[water] -= bev[water]
    data[milk] -= bev[milk]
    data[coffee] -= bev[coffee]
    data[money] += bev[money]

def change(bev):
    """Handles payment and returns whether the transaction was successful."""
    print("Please insert coins.")
    quart = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    
    pay = quart * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if bev[money] == pay:
        return True
    if bev[money] > pay:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    if bev[money] < pay:
        change_amt = pay - bev[money]
        print(f"Here is your change: ${change_amt:.2f}")
        data[money] += bev[money]  # Add only the beverage cost to the machine
        return True

def make_latte():
    if check_resources(latte):
        if change(latte):
            deduct(latte)
            print("Here is your latte! ☕ Enjoy!")

def make_espresso():
    if check_resources(espresso):
        if change(espresso):
            deduct(espresso)
            print("Here is your espresso! ☕ Enjoy!")

def make_cappuccino():
    if check_resources(cappuccino):
        if change(cappuccino):
            deduct(cappuccino)
            print("Here is your cappuccino! ☕ Enjoy!")

# Coffee machine loop
while True:
    choice = input("What would you like? (1: espresso, 2: latte, 3: cappuccino, 'report', 'quit'): ").lower()

    if choice == "1":
        make_espresso()
    elif choice == "2":
        make_latte()
    elif choice == "3":
        make_cappuccino()
    elif choice == "report":
        report()
    elif choice == "quit":
        print("Thank you, goodbye!")
        break
    else:
        print("Invalid input. Please choose again.")
