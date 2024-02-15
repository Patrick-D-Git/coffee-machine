from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()  # coffeeMaker class , coffee_machine object
coffee_menu = Menu()  # Menu class, coffee_menu object
money_dispenser = MoneyMachine()  # MoneyMachine class , money_dispenser object


coffee_machine_on = True

while coffee_machine_on:

    user_coffee_choice = input("What would you like? 'espresso/latte/cappuccino': ")

    if user_coffee_choice == "off":
        coffee_machine_on = False
    elif user_coffee_choice == "report":
        coffee_machine.report()
        money_dispenser.report()
    else:
        # Finds the drink information and assign it to 'drink'
        drink = coffee_menu.find_drink(user_coffee_choice)

        if coffee_machine.is_resource_sufficient(drink):  # checks if it has enough ingredients/resource
            if money_dispenser.make_payment(drink.cost):  # checks money received
                coffee_machine.make_coffee(drink)  # creates the coffee
