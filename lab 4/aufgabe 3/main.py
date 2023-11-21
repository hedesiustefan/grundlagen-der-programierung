

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper ,scissors]

#player choice
def player():
    player_choice = input("What do you choose? Type 0 for Rock , 1 for Papper or 2 for Scissors ")
    while player_choice not in ['0','1','2']:
        print("Please pick from 0, 1 or 2")
        player_choice = input("Your choice ")
    player_choice = int(player_choice)
    return player_choice



#random comp choice
def comp():
    comp_choice = random.randint(0,2)
    return comp_choice


#win/lose casses
def game(player_choice, comp_choice):
    if player_choice == 0 and comp_choice == 2:
        return "loss"
    if comp_choice == 0 and player_choice == 2:
        return "win"
    elif comp_choice > player_choice:
        return "win"
    elif comp_choice == player_choice:
        return "draw"
    elif comp_choice < player_choice:
        return "loss"





def main():
    countplayer = 0
    countcomp = 0
    for i in range(3):
        comp_choice = comp()
        player_choice = player()
        print(game_images[player_choice])
        print(f'The computer chose {comp_choice}')
        print(game_images[comp_choice])
        if game(comp_choice,player_choice) == "loss":
            countcomp += 1
            print('The computer won this round.')
        if game(comp_choice,player_choice) == "win":
            countplayer += 1
            print('The player won this round.')
        if game(comp_choice,player_choice) == "draw":
            print('No one won this round.')
    if countplayer > countcomp:
            print("U are the winner!")
    elif countplayer < countcomp:
            print("U lost....")
    else:
            print("Equal game")

main()