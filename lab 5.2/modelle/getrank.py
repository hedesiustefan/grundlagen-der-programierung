from modelle.gericht import Gericht

class Getrank(Gericht):

    def __init__(self, id, price, alcohol):
        super().__init__(id, price)
        self.alcohol = alcohol

    def __lt__(self, other):
        return self.id < other.id

    def __iter__(self):
        return iter(self.id, self.price)

    def __str__(self):
        return f"{self.id}    {self.price} Euro    {self.alcohol}% alcohol"