from repository.data_repo import CookedDishRepo, DrinkRepo
from modelle.gekochter_gericht import GekochterGericht
from modelle.getrank import Getrank
from controller.data_logik import display_data

dish_manager = CookedDishRepo()
drink_manager = DrinkRepo()


def display_menu():
    print("Gerichte: ")
    display_data(0)

    print("Getränke: ")
    display_data(1)


def add_dish():
    name = input("Name der Gericht: ")
    price = int(input("Preis der Gericht: "))
    zeit = int(input("Kochzeit: "))

    dishes = dish_manager.load() if dish_manager.load() else []
    dish = GekochterGericht(name, price, zeit)
    dishes.append(dish)
    dish_manager.sort(dishes)


def add_drink():
    name = input("Name der Getränk: ")
    price = int(input("Preis der Getränk: "))
    alcohol = input("Alcohol Einhalt: ")

    drinks = drink_manager.load() if drink_manager.load() else []
    drink = Getrank(name, price, alcohol)
    drinks.append(drink)
    drink_manager.sort(drinks)


def search_item():
    name = input("Name der Item die sie suchen wollen: ")
    dishes = dish_manager.load() if dish_manager.load() else []
    drinks = drink_manager.load() if drink_manager.load() else []
    print('\n')
    if dishes:
        print("Gerichte: ", '\n')
        for index in range(len(dishes)):
            if name.lower() in dishes[index].id.lower():
                print(index, str(dishes[index]))

    if drinks:
        print("Drinks: ", '\n')
        for index in range(len(drinks)):
            if name.lower() in drinks[index].id.lower():
                print(index, str(drinks[index]))

        return

    print("Es gibt kein Item mit den gegebenen Name")


def update_item():
    type = int(input("""
        Tragen sie der Typ der Item ein(update): 
            1 - Gericht
            2 - Getränk
        """))

    id = int(input("Tragen sie das ID der Item ein: "))

    if type == 1:
        name = input("Neuen Name der Gericht: ")
        price = input("Neuen Preis der Gericht: ")
        prepTime = input("Neuen Kochzeit der Gericht: ")
        dish = GekochterGericht(name, price, prepTime)
        drink_manager.update(id, dish)
    else:
        name = input("Neuen Name der Getränk: ")
        price = input("Neuen Preis der Getränk: ")
        alcohol = input("Neuen Alcohol Einhalt der Getränk: ")
        drink = Getrank(name, price, alcohol)
        drink_manager.update(id, drink)


def show_menu_update():
    display_menu()
    update_item()


def deleteItem():
    type = int(input("""
        Tragen sie der Typ der Item ein(delete): 
            1 - Gericht
            2 - Getränk
        """))

    id = int(input("Tragen sie das ID der Item ein: "))

    if type == 1:
        dish_manager.remove(id)
    else:
        drink_manager.remove(id)


def show_menu_delete():
    display_menu()
    deleteItem()
