from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

till = MoneyMachine()
starbuck = CoffeeMaker()
menu = Menu()

while True:
    order = input(f'please make a selection: {menu.get_items()}  ? ')
    if order == 'report':
        starbuck.report()
        till.report()
        continue
    elif order == 'off':
        print('Shutting down...')
        exit(0)
    drink = menu.find_drink(order)
    if drink is None:
        continue
    else:
        if starbuck.is_resource_sufficient(drink):
            print(f"Please insert ${drink.cost}")
            accepted = till.make_payment(drink.cost)
            if accepted:
                starbuck.make_coffee(drink)
   