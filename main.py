MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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

money = 0

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

def check_resources(order_ingredients):
    '''checks if there's sufficient resources to cover the order.'''
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    total = int(input("How many 50 cent coins?: "))* 0.50
    total += int(input("How many $1 coins?: "))* 1
    total += int(input("How many $2 coins?: ")) * 2
    return total

def payment_success(coin_total, order_cost):
    if coin_total >= order_cost:
        change = "%.2f"%round(coin_total - order_cost, 2)
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Insufficient funds. Please try again.")
        return False

def use_resources(order_ingredients, order):
    '''subtracts order ingredients from available resources.'''
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Enjoy your {order}! ☕️")

machine_on = True
while machine_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "report":
        report()
    elif order == "off":
        print("Machine off")
        machine_on = False
    else:
        order_ingredients = MENU[order]["ingredients"]
        order_cost = MENU[order]["cost"]
        if check_resources(order_ingredients):
            print(f"Cost: ${MENU[order]['cost']}. Please insert coins:")
            coin_total = process_coins()
            if payment_success(coin_total, order_cost):
                use_resources(order_ingredients, order)
                money += order_cost