from store import resources, MENU

money = 0
machine_on = True


# TODO print all the available for
def report():
    print(F"Water: {resources['water']}ml"
          F" \nMilk: {resources['milk']}ml"
          F" \nCoffee: {resources['coffee']}g"
          F" \nMoney: ${money} ")


# TODO 3 check if resources are sufficient
def resources_sufficient(coffe_choice):
    """
    This checks if there are enough resource to make the selected choice of coffee then returns True or False
    :param coffe_choice:
    :return:
    """
    drink = MENU[coffe_choice]
    order_ingredients = drink['ingredients']
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def calculate_coin():
    """
    This return the total value of coins inserted.
    """
    print("Please insert coin")
    total = int(input("How many dimes?: ")) * 0.1
    total += int(input("How many quarters?: ")) * 0.25
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def confirm_transaction(money_received, drink_price):
    if money_received < drink_price:
        print("Sorry that's not enough money. Money refunded")
        return False
    else:
        global money
        change = round(money_received - drink_price, 2)
        money += drink_price
        print(f"Take your change of ${change}")
        return True


def make_coffee(drink_name, order_ingredients):
    """This deducts the amount of coffee resources from the available resources
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {user_choice} coffee 🍵🍵🍵🍵. Enjoy")


while machine_on:
    # TODO prompt user asking what they will like to order?
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if user_choice == 'off':
        machine_on = False
    elif user_choice == 'report':

        report()
    else:
        if resources_sufficient(user_choice):
            payment = calculate_coin()
            drink = MENU[user_choice]
            drink_cost = drink['cost']
            if confirm_transaction(money_received=payment, drink_price=drink_cost):
                make_coffee(drink_name=user_choice, order_ingredients= drink['ingredients'])

