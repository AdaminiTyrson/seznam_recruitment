
from source_data import MENU
from source_data import resources


espresso_price = MENU["espresso"]["cost"]
latte_price = MENU["latte"]["cost"]
cappuccino_price = MENU["cappuccino"]["cost"]

#funkce
def report(data):
    print(f"Voda: {data['water']}")
    print(f"Mléko: {data['milk']}")
    print(f"Káva: {data['coffee']}")

def coins ():
    print ("Prosím vložte CZK mince 1, 2, 5, 10, 20, 50")
    kc_1 = int(input("Kolik 1 Kč mincí chcete vložit?: ")) * 1
    kc_2 = int(input("Kolik 2 Kč mincí chcete vložit?: ")) * 2
    kc_5 = int(input("Kolik 5 Kč mincí chcete vložit?: ")) * 5
    kc_10 = int(input("Kolik 10 Kč mincí chcete vložit?: ")) * 10
    kc_20 = int(input("Kolik 20 Kč mincí chcete vložit?: ")) * 20
    kc_50 = int(input("Kolik 50 Kč mincí chcete vložit?: ")) * 50
    suma = (kc_1 + kc_2 + kc_5 + kc_10 + kc_20 + kc_50)
    print (f"Celkem jste vložili: {suma} Kč")
    return suma

def calculate_change(user_sum_coins, price):
    refund = user_sum_coins - price
    if refund >= 0:
        print("Nápoj se připravuje.")
        if refund > 0:
            print (f"vráceno: {refund}")
    else:
        print(f"Nevhodil jste dostatek peněž. Vložte ještě {price - user_sum_coins} Kč")

def fill_in_ingredients():
    return resources

def calculate_ingredients(drink_name):
    if drink_name == "espresso":
        rest_ingredients["water"] = rest_ingredients["water"] - MENU["espresso"]["ingredients"]["water"]
        rest_ingredients["milk"] = rest_ingredients["milk"] - MENU["espresso"]["ingredients"]["milk"]
        rest_ingredients["coffee"] = rest_ingredients["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
        print (f"Zbylé ingredience {rest_ingredients}")
    elif drink_name == "latte":
        rest_ingredients["water"] = rest_ingredients["water"] - MENU["latte"]["ingredients"]["water"]
        rest_ingredients["milk"] = rest_ingredients["milk"] - MENU["latte"]["ingredients"]["milk"]
        rest_ingredients["coffee"] = rest_ingredients["coffee"] - MENU["latte"]["ingredients"]["coffee"]
        print(f"Zbylé ingredience {rest_ingredients}")
    elif drink_name == "cappuccino":
        rest_ingredients["water"] = rest_ingredients["water"] - MENU["cappuccino"]["ingredients"]["water"]
        rest_ingredients["milk"] = rest_ingredients["milk"] - MENU["cappuccino"]["ingredients"]["milk"]
        rest_ingredients["coffee"] = rest_ingredients["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
        print(f"Zbylé ingredience {rest_ingredients}")


def ingredients_checker(in_water, in_milk, in_coffee):
    if in_water < 0:
        print("Není dostatek ingrediencí na tento nápoj")
        return False
    elif in_milk < 0:
        print("Není dostatek ingrediencí na tento nápoj")
        return False
    elif in_coffee < 0:
        print("Není dostatek ingrediencí na tento nápoj")
        return False
    else:
        print ("Na nápoj máme dostatek ingrediencí.")
        return True

# Kód automatu
# Načítáme původní množství ingrediencí
rest_ingredients = fill_in_ingredients()

lets_continue = True

while(lets_continue):
    user_choise = input("Co byste si dal? Espresso / Latte / Cappuccino ?").lower()

    # Kolik zbývá ingrediencí
    calculate_ingredients(user_choise)

    # Kontrola zůstatku ingrediencí
    if user_choise != "report":
        lets_continue = ingredients_checker(rest_ingredients["water"], rest_ingredients["milk"], rest_ingredients["coffee"])

    # Má kód dále pokračovat?
    if lets_continue == False:
        break

    # Kontrolní report
    if user_choise == "report":
        report(rest_ingredients)

    if user_choise == "espresso":
        sum = coins()
        print (f"Cena espressa je: {espresso_price}")
        calculate_change(sum, espresso_price)

    elif user_choise == "latte":
        sum = coins()
        print(f"Cena latté je: {latte_price}")
        calculate_change(sum, latte_price)

    elif user_choise == "cappuccino":
        sum = coins()
        print (f"Cena cappuccina je: {cappuccino_price}")
        calculate_change(sum, cappuccino_price)
