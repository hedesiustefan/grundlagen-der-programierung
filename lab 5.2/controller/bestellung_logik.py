from repository.data_repo import OrderRepo, CustomerRepo
from controller.kunde_logik import add_costumers
from controller.menu_logik import drink_manager, dish_manager, display_menu
from controller.data_logik import display_data
from modelle.bestellung import Order

order_manager = OrderRepo()
customer_manager = CustomerRepo()


def search_customer_name():
    name = input("Tragen sie die Name der Kunde ein: ")
    customers = customer_manager.load() if customer_manager.load() else []
    print('\n')
    ids = []
    if customers:
        print("Kunden: ", '\n')
        for index in range(len(customers)):
            if name.lower() in customers[index].name.lower():
                print(index, str(customers[index]))
                ids.append(customers[index].id)


def search_customer_address():
    address = input("Tragen sie die Name der Item ein: ")
    customers = customer_manager.load() if customer_manager.load() else []
    print('\n')
    if customers:
        print("Kunden: ", '\n')
        for index in range(len(customers)):
            if address.lower() in customers[index].address.lower():
                print(index, str(customers[index]))


def add_user_order():
    print('\n', "Kunden:")
    display_data(2)
    add_costumers()


def new_order():
    value = int(input("ID der Kunde der zu die Order gehört. "))
    customers = customer_manager.load() if customer_manager.load() else []
    customer = customers[value]

    dishIds = []
    drinkIds = []
    dishes = dish_manager.load() if dish_manager.load() else []
    drinks = drink_manager.load() if drink_manager.load() else []

    print("Wahlen sie was zu die Order gehören soll, taste -1 um mit die Order fortzusetzen: ", '\n')
    display_menu()

    while True:
        type = int(input("""
        Wählen sie das Art der Gericht:
            1 - Gekochter Gericht
            2 - Getränk
        """))

        if type == -1:
            break

        if type == 1:
            id = int(input("ID: "))
            if id < len(dishes):
                dishIds.append(dishes[id].id)
            else:
                print("ID nicht gefunden")
        else:
            id = int(input("ID: "))
            if id < len(drinks):
                drinkIds.append(drinks[id].id)
            else:
                print("ID nicht gefunden")

    order = Order(1, customer.id, dishIds, drinkIds)
    orders = order_manager.load() if order_manager.load() else []
    orders.append(order)
    order_manager.sort(orders)

    order.displayInvoice()


def display_orders():
    print("Bestellungen: ")
    display_data(3)

    orders = order_manager.load()
    value = int(input("ID der Order fur die Rechnung: "'\n'))
    orders[value].displayInvoice()