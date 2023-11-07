import random

def computer():
    wahl = ['Stein','Schere','Papier']
    wahl = random.choice(wahl)
    return wahl

def player():
    while True:
        v1 = input("Wahle aus (Stein,Schere,Papier):").strip().capitalize()
        if v1 in ['Stein','Schere','Papier']:
            return v1
        else:
            print("Bitte wahlen sie etwas aus der Liste" )

def game(v1,wahl):
    if v1 == wahl:
        return 'Gleicheit'
    elif (wahl == 'Schere' and v1 == 'Stein' ) or (wahl == 'Stein' and v1 == 'Papier') or (wahl == 'Papier' and v1 == 'Schere'):
        return 'Player gewinnt'
    else:
        return 'Computer gewinnt'

def main():
    countwahl = 0
    countv1 = 0
    for i in range(3):
        wahl = computer()
        v1 = player()
        print(wahl)
        if game(wahl,v1) == 'Computer gewinnt':
            countwahl += 1
        if game(wahl,v1) == 'Player gewinnt':
            countv1 += 1
        if countv1 > countwahl:
            print("Du hast gewonnen")
        elif countv1 < countwahl:
            print("PC hat gewonnen")
        else:
            print("Egalitaet")

