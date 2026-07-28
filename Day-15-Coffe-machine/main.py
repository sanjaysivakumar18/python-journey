MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

resources = {
    "water": 500,
    "milk": 300,
    "coffee": 100,
}

money = 0


def display_report():
    """Print current resources."""
    print("\n------ Coffee Machine Report ------")
    print(f"Water : {resources['water']} ml")
    print(f"Milk  : {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money : ₹{money}")
    print("-----------------------------------\n")


def resources_available(drink):
    """Check whether enough ingredients are available."""
    required = MENU[drink]["ingredients"]

    for item in required:
        if resources[item] < required[item]:
            print(f"Sorry! Not enough {item}.")
            return False

    return True


def collect_money():
    """Ask user for coins and return total amount."""

    print("\nInsert Coins")

    ten = int(input("₹10 coins: "))
    twenty = int(input("₹20 coins: "))
    fifty = int(input("₹50 coins: "))
    hundred = int(input("₹100 notes: "))

    total = (ten * 10) + (twenty * 20) + (fifty * 50) + (hundred * 100)

    return total


def process_payment(amount_given, drink):
    """Verify payment and return True if successful."""

    global money

    cost = MENU[drink]["cost"]

    if amount_given < cost:
        print("Not enough money. Refunding payment.")
        return False

    change = amount_given - cost

    if change > 0:
        print(f"Please collect your change: ₹{change}")

    money += cost
    return True


def prepare_coffee(drink):
    """Deduct ingredients and serve coffee."""

    ingredients = MENU[drink]["ingredients"]

    for item in ingredients:
        resources[item] -= ingredients[item]

    print(f"\n☕ Your {drink.title()} is ready. Enjoy!\n")


machine_on = True

while machine_on:

    choice = input(
        "What would you like? (espresso/latte/cappuccino): "
    ).lower()

    if choice == "off":
        machine_on = False
        print("Coffee machine turned off.")

    elif choice == "report":
        display_report()

    elif choice in MENU:

        if resources_available(choice):

            payment = collect_money()

            if process_payment(payment, choice):
                prepare_coffee(choice)

    else:
        print("Invalid option. Please try again.")