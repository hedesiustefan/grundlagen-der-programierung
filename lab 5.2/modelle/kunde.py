from modelle.identifizierbar import Identifizierbar


class Kunde(Identifizierbar):

    def __init__(self, id, name, adresse):
        super().__init__(id)
        self.name = name
        self.adresse = adresse

    def __lt__(self, other):
        return self.name < other.name

    def __str__(self):
        return f'{self.id}   {self.name}   {self.adresse}'
