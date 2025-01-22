# written by M7md-5shbh
# Performs functions and calculations of a coffee machine
#--------------------------------------------

menu = {
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def payment(item):
    print("Please Insert Coins.")
    quarter = int(input("How many quarters? "))
    dime = int(input("How many dimes? "))
    nickle = int(input("How many nickles? "))
    penny = int(input("How many pennies? "))
    amount = (quarter * 0.25) + (dime * 0.10) + (nickle * 0.05) + (penny * 0.01)
    if amount < menu[item]["cost"]:
        return False
    else:
        return round(amount - menu[item]["cost"], 2)

def make_drink(drink):
    insufficient_resources = False
    drinks = ["espresso", "latte", "cappuccino"]
    drink_index = drinks.index(drink)
    for item in drinks:
        if drinks[drink_index] == item:
            for key, ingredient in menu[drink]["ingredients"].items():
                if ingredient >= resources[key]:
                    print(f"There's not enough {key} to make the drink")
                    insufficient_resources = True
            if not insufficient_resources:
                change = payment(drink)
                print(f"Here's your change: ${change}")
            for key, ingredient in menu[drink]["ingredients"].items():
                resources[key] -= ingredient
        else:
            continue

def coffeeMachine():
    done = False
    can_make_order = True
    while not done:
        user_drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_drink == "off":
            done = True
        elif user_drink == "report":
            for key, value in resources.items():
                print(f"{key}: {value}")
        else:
            make_drink(user_drink)

coffeeMachine()
