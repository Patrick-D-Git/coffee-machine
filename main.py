from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
coffee_menu = Menu()
money_dispenser = MoneyMachine()


coffee_machine_on = True

while coffee_machine_on:

    user_coffee_choice = input("What would you like? 'espresso/latte/cappuccino': ")

    if user_coffee_choice == "off":
        coffee_machine_on = False
    elif user_coffee_choice == "report":
        coffee_machine.report()
    else:
        drink = coffee_menu.find_drink(user_coffee_choice)

        if coffee_machine.is_resource_sufficient(drink):
            if money_dispenser.make_payment(money_dispenser.money_received):
                coffee_machine.make_coffee(drink)
