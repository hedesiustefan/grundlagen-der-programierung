from modelle.gericht import Gericht

class GekochterGericht(Gericht):
    def __init__(self, id, price, zeit):
        super().__init__(id, price)
        self.zeit = zeit

    def __lt__(self, other):
        return self.id < other.id

    def __iter__(self):
        return iter(self.id, self.price)

    def __str__(self):
        return f"{self.id}   {self.price} {self.zeit}"