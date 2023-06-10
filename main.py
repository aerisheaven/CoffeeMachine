from decimal import Decimal

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
}


def print_report():
    for key in resources:
        print(f"{key}: {resources[key]}", end="")
        if key == "Water" or key == "Milk":
            print("ml")
        else:
            print("g")
    print(f"Money: ${money}")


def take_order():
    if MENU[order]["ingredients"]["water"] > resources["Water"]:
        print("Sorry, there is not enough water.")
    elif order != "espresso" and MENU[order]["ingredients"]["milk"] > resources["Milk"]:
        print("Sorry, there is not enough milk.")
    elif MENU[order]["ingredients"]["coffee"] > resources["Coffee"]:
        print("Sorry, there is not enough coffee.")
    else:
        resources["Water"] -= MENU[order]["ingredients"]["water"]
        if order != "espresso":
            resources["Milk"] -= MENU[order]["ingredients"]["milk"]
        resources["Coffee"] -= MENU[order]["ingredients"]["coffee"]
        money_var = process_coins()
        return money_var


def process_coins():
    print("Please insert coins.")
    num_quarters = int(input("How many quarters?: "))
    num_dimes = int(input("How many dimes?: "))
    num_nickels = int(input("How many nickels?: "))
    num_pennies = int(input("How many pennies?: "))
    total = (num_quarters * QUARTER) + (num_dimes * DIME) + (num_nickels * NICKEL) + (num_pennies * PENNY)
    if total < MENU[order]["cost"]:
        print("Sorry, that's not enough money. Money refunded.")
    else:
        money_var = calculate_change(total)
        print(f"Here is your {order}. Enjoy!")
        return money_var


def calculate_change(total):
    change = round(Decimal(total - MENU[order]["cost"]), 2)
    print(f"Here is ${change} in change.")
    return total - float(change)


QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01

money = 0
print("Welcome to the Digital Python Coffee Machine.")
machine_on = True
while machine_on:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "report":
        print_report()
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        money += take_order()
    elif order == "off":
        machine_on = False
