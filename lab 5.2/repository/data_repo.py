import pickle


class DataRepo:

    def __init__(self):
        self.filename = None

    def save(self, object_list):
        with open(self.filename, 'wb') as file:
            pickle.dump(object_list, file)

    def load(self):
        with open(self.filename, 'rb') as file:
            try:
                return pickle.load(file)
            except EOFError:
                print("Nichts wurde gefunden")

    def sort(self, object_list):
        object_list = sorted(object_list)
        self.save(object_list)

    def add(self, obj):
        object_list = self.load()
        object_list.append(obj)
        self.sort(object_list)
        print("Item wurde eingeladen")

    def remove(self, id):
        object_list = self.load()
        if id < len(object_list):
            object_list.pop(id)
            self.save(object_list)
            print("Item mit dem gegebenen ID wurde gelöst")
            return

        print("Item mit dem gegebenen ID wurde nicht gefunden")

    def update(self, id, new_obj):
        object_list = self.load()
        if id < len(object_list):
            self.remove(id)
            self.add(new_obj)
            return

        print("Item mit dem gegebenen ID wurde nicht gefunden")


class OrderRepo(DataRepo):
    def __init__(self):
        super().__init__()
        self.filename = 'repository/data/order.dat'


class CustomerRepo(DataRepo):
    def __init__(self):
        super().__init__()
        self.filename = 'repository/data/customer.dat'


class DrinkRepo(DataRepo):
    def __init__(self):
        super().__init__()
        self.filename = 'repository/data/drink.dat'


class CookedDishRepo(DataRepo):
    def __init__(self):
        super().__init__()
        self.filename = 'repository/data/cooked_dish.dat'
