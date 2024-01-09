from modelle.identifizierbar import Identifizierbar


class Gericht(Identifizierbar):
    portion = 400

    def __init__(self, id, price):
        super().__init__(id)
        self.price = price