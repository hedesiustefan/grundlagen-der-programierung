from controller.menu_logik import display_menu, add_dish, add_drink, search_item, show_menu_update, show_menu_delete
from controller.kunde_logik import get_costumers, add_costumers, update_costumer, delete_costumer
from controller.bestellung_logik import (search_customer_name, search_customer_address, new_order, display_orders,
                                         add_user_order)


def default_interface():
    options = {
        1: menu_interface,
        2: customer_interface,
        3: order_interface
    }

    while True:
        print("""
        Welcome to the best Restaurant press any of the following keys to continue:
            1 - Menu
            2 - Kunden
            3 - Bestellung
            0 - Exit 
        """)

        value = int(input())

        if value == 0:
            exit()

        options[value]()


def type_of_item():
    value = int(input("""
    Typ der Item
        1 - Gericht
        2 - Getränk
    """))

    options = {
        1: add_dish,
        2: add_drink
    }

    options[value]()
    print("Der Artikel wurde erfolgreich hinzugefügt")
    menu_interface()


def menu_interface():
    while True:
        value = int(input("""
        
        Wählen Sie eine Option aus:
            1 - View the menu
            2 - Search for an item in the menu
            3 - Add a new item to the menu
            4 - Update an existing menu item 
            5 - Delete an existing menu item
            0 - Back        
        """))

        options = {
            1: display_menu,
            2: search_item,
            3: type_of_item,
            4: show_menu_update,
            5: show_menu_delete,
            0: default_interface
        }

        options[value]()

        menu_interface()


def customer_interface():
    while True:
        value = int(input("""
           Wählen Sie eine Option aus:
               1 - Alle Kunden anzeigen
               2 – Einen neuen Kunden hinzufügen
               3 – Aktualisieren Sie einen bestehenden Kunden
               4 – Löschen Sie einen bestehenden Kunden
               0 - Back      
           """))

        options = {
            1: get_costumers,
            2: add_costumers,
            3: update_costumer,
            4: delete_costumer,
            0: default_interface
        }

        options[value]()

        customer_interface()


def order_interface():
    while True:
        value = int(input("""
           Wählen Sie eine Option aus:
               1 – Fügen Sie eine neue Bestellung hinzu
               2 - Frühere Bestellungen anzeigen
               0 - Back     
           """))

        options = {
            1: select_customer_interface,
            2: display_orders,
            0: default_interface
        }

        options[value]()


def select_customer_interface():
    value = int(input("""
         Wählen Sie eine Option aus:
            1 - Suchen Sie nach einem Kunden anhand seines Namens
            2 - Suchen Sie nach einem Kunden anhand der Adresse
            3 – Einen neuen Kunden hinzufügen
            0 - Back
    """))

    options = {
        1: search_customer_name,
        2: search_customer_address,
        3: add_user_order,
        0: order_interface
    }

    options[value]()

    new_order()
