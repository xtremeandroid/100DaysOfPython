from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee1 = CoffeeMaker()
moneyMachine1 = MoneyMachine()
is_on = True

while is_on:
    choice = input(f"What would you like? {menu.get_items()}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee1.report()
        moneyMachine1.report()
    else:
        drink = menu.find_drink(choice)
        if coffee1.is_resource_sufficient(drink):
            if moneyMachine1.make_payment(drink.cost):
                coffee1.make_coffee(drink)
            else:
                print("Insufficient payment, money refunded")
