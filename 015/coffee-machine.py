#! /usr/bin/env python3

from simple_term_menu import TerminalMenu
import os

# The purpose of this project isn't to make a fully functional coffee machine, rather test pycharm features
# Some PyCharm notable features: To Do feature, spell checker, function and variable explorer, linting...

# TODO: Continue exploring PyCharm features
# TODO: Test and Debug


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


plugged_in = True

money_made = 0

# TODO: Add more coffee types
coffee = {
    "cappuccino": {
        "coffee": 24,
        "milk": 100,
        "water": 250,
        "cost": 0.15,
    },
    "expresso": {
        "coffee": 18,
        "milk": 0,
        "water": 50,
        "cost": 0.10,
    },
    "latte": {
        "coffee": 24,
        "milk": 150,
        "water": 200,
        "cost": 0.25,
    },
}

resources = {
    'coffee': 1000,  # g, grams
    'milk': 2000,  # ml, milli-litters
    'water': 3000,  # ml, milli-litters
    'cost': 0.0,  # $ the current money deposited
}

money = {
    'penny': 0.01,
    'nickel': 0.05,
    'dime': 0.10,
    'quarter': 0.25,
    'done': 0,  # Used to end depositing money
}

ascii_art = {
    'cappuccino': """
      )  (
     (   ) )
      ) ( (
    _______)_
 .-'---------|  
( C|/\/\/\/\/|
 '-./\/\/\/\/|
   '_________'
    '-------'
""",
    'expresso': """
    _____
   |-----|  
   '_____'
    '---'
""",
    'latte': """
     _______ 
 .-'-__<3___-|  
( C|/\/\/\/\/|
 '-./\/\/\/\/|
   '_________'
    '-------'
""",
}


def check_sufficient_resources(desired_coffee):
    # Iterate over each resource required for the desired coffee
    for resource, amount in coffee.get(desired_coffee).items():
        # print(resource, amount)
        if resources.get(resource) < amount:
            print(f"Not enough resource of {resource}")
            print(f"Current {resource} level: {resources.get(resource)}")
            input(f"Press enter to acknowledge")

            return False
    return True


def resolve_resource(resource):
    global resources
    if resource == "coffee":
        return 100
    if resource == "milk":
        return 200
    if resource == "water":
        return 300
    if resource == "cost":
        prompt_to_deposit_money()


def prompt_to_deposit_money():
    coin_inserted = True
    while coin_inserted:
        money_deposited = deposit_money()
        if money_deposited > 0:
            resources['cost'] += money_deposited
        elif money_deposited == 0:
            coin_inserted = False


def print_coffee_maker_menu():
    coffee_maker_menu_options = [
        'Select a Coffee to Make',
        'Reports',
        'Resources'
    ]
    print(f"Money Deposited: {resources.get('cost')}")
    coffee_maker_menu = TerminalMenu(
        coffee_maker_menu_options,
        title=f"What kind of coffee do you want?"
    )
    coffee_maker_menu_index = coffee_maker_menu.show()
    # coffee_maker_menu_selected = list(coffee.keys())[coffee_maker_menu_index]

    if coffee_maker_menu_index == 0:  # Select a Coffee to Make
        clear()
        print_desired_coffee_menu()
    elif coffee_maker_menu_index == 1:  # Reports
        clear()
        print_report()
    elif coffee_maker_menu_index == 2:  # Resources
        clear()
        resource_menu_list = list(resources.keys())
        for r in resource_menu_list:
            print(f"{r:<16} {resources.get(r)}")

        resources_menu = TerminalMenu(
            resource_menu_list,
            title='Which resource would you like to fill?'
        )
        resources_menu_index = resources_menu.show()
        resources_menu_selected = resource_menu_list[resources_menu_index]
        resources[resources_menu_selected] = resolve_resource(resources_menu_selected)


def deposit_money():
    print(f"Money Deposited: {resources['cost'] }")
    deposit_money_menu = TerminalMenu(
        list(money.keys()),
        title=f"What type of money do you deposit?"
    )
    deposit_money_index = deposit_money_menu.show()
    deposit_money_selected = list(money.keys())[deposit_money_index]
    for coin, value in money.items():
        if coin == deposit_money_selected:
            return value


def print_report():
    # Shows all resources and money
    for key, value in resources.items():
        print(f"{key:<16} {value}")
    print(f"{'Money Made:':<16} {money_made}")


def print_desired_coffee_menu():
    for coffee_type in coffee.keys():
        # print(f"{coffee_type}")
        print(f"{coffee_type:<16} {coffee.get(coffee_type)['cost']}")

    desired_coffee_menu = TerminalMenu(
        list(coffee.keys()),
        title=f"What kind of coffee do you want?"
    )
    desired_coffee_index = desired_coffee_menu.show()
    desired_coffee_selected = list(coffee.keys())[desired_coffee_index]

    prompt_to_deposit_money()

    global money_made
    # TODO: Optimize the code below
    if check_sufficient_resources(desired_coffee_selected):
        clear()
        if desired_coffee_selected == "cappuccino":
            resources['coffee'] -= coffee['cappuccino']['coffee']
            resources['milk'] -= coffee['cappuccino']['milk']
            resources['water'] -= coffee['cappuccino']['water']
            resources['cost'] -= coffee['cappuccino']['cost']
            money_made += coffee['cappuccino']['cost']
            print(ascii_art.get('cappuccino'))
        if desired_coffee_selected == "expresso":
            resources['coffee'] -= coffee['expresso']['coffee']
            resources['milk'] -= coffee['expresso']['milk']
            resources['water'] -= coffee['expresso']['water']
            resources['cost'] -= coffee['expresso']['cost']
            money_made += coffee['expresso']['cost']
            print(ascii_art.get('expresso'))
        if desired_coffee_selected == "latte":
            resources['coffee'] -= coffee['latte']['coffee']
            resources['milk'] -= coffee['latte']['milk']
            resources['water'] -= coffee['latte']['water']
            resources['cost'] -= coffee['latte']['cost']
            money_made += coffee['latte']['cost']
            print(ascii_art.get('latte'))
    else:
        clear()
        print(f"Not enough resources to make a {desired_coffee_selected}. ")


def main():
    while plugged_in:
        print_coffee_maker_menu()


if __name__ == "__main__":
    main()
