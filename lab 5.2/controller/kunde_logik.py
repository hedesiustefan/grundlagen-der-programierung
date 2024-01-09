from repository.data_repo import CustomerRepo, OrderRepo
from controller.data_logik import display_data
from modelle.kunde import Kunde

costumer_manager = CustomerRepo()


def get_costumers():
    print("Kunden: ")
    display_data(2)


def add_costumers():
    name = input("Name der Kunde: ")
    address = input("Adresse der Kunde: ")

    customers = costumer_manager.load() if costumer_manager.load() else []
    costumer = Kunde(1, name, address)
    customers.append(costumer)
    costumer_manager.sort(customers)


def update_costumer():
    get_costumers()
    list_id = int(input("Tragen sie das id ein: "))
    costumers = costumer_manager.load()

    id = costumers[list_id].id
    name = input("Tragen sie die Name ein: ")
    address = input("Tragen sie die Adresse ein: ")
    costumer = Kunde(id, name, address)
    costumer_manager.update(list_id, costumer)


def delete_costumer():
    get_costumers()
    order_manager = OrderRepo()
    orders = order_manager.load()
    costumers = costumer_manager.load()
    id = int(input("Tragen sie das id der Kunde ein: "))

    for index in range(len(orders)):
        if orders[index].customerId == costumers[id].id:
            order_manager.remove(index)

    costumer_manager.remove(id)
