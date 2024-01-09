from modelle.identifizierbar import Identifizierbar
from controller.menu_logik import dish_manager, drink_manager
from functools import reduce


class Order(Identifizierbar):
    total = 0

    def __init__(self, id, customer_id, dishes, drinks):
        super().__init__(id)
        self.customerId = customer_id
        self.dishes = dishes
        self.drinks = drinks

    def calculateCosts(self):
        dish_list = dish_manager.load()
        drink_list = drink_manager.load()
        prices = []

        for dish in dish_list:
            if dish.id in self.dishes:
                prices.append(int(dish.price))

        for drink in drink_list:
            if drink.id in self.drinks:
                prices.append(int(drink.price))

        self.total = reduce(lambda x, y: x + y, prices)

    def generateInvoice(self):
        self.calculateCosts()
        dishList = dish_manager.load()
        drinkList = drink_manager.load()
        invoice = f"Bestellung: {self.id} für der Kunde mid dem ID: {self.customerId}" + '\n'

        names = []
        prices = []

        for dish in dishList:
            if dish.id in self.dishes:
                names.append(dish.id)
                prices.append(str(dish.price))

        for drink in drinkList:
            if drink.id in self.drinks:
                names.append(drink.id)
                prices.append(str(drink.price))

        items = list(map(lambda x, y: f"Item: {x}     Preis: {y} Euro" + '\n', names, prices))

        invoice += "".join(items)
        invoice += f"Total: {str(self.total)} Euro"

        return invoice

    def displayInvoice(self):
        invoice = self.generateInvoice()
        print(invoice)

    def __lt__(self, other):
        return self.id < other.id

    def __str__(self):
        return f'Bestellung: {self.id}   Kunde: {self.customerId}   Gerichte: {self.dishes}   Getränke: {self.drinks}'