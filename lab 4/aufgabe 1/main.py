from menu import *
from costum_buchstaben import draw
from word_to_draw import draw_automatic
def main():
   with open('save_commands.txt', 'a') as file:
       file.write("\n")
   while True:
        print(meniu())
        opt = int(input("Optiunea="))

        if opt == 1:
            draw_automatic()
        if opt == 2:
            draw()
        if opt == 0:
            break

main()
