#Simple dice rolling CLI program.
#Type 'y' or 'Y' (for yes) to output a random number.

#Written by Caleb Phillips (LebbyFoxx).
#Saturday 26th September 2020.

import random
import sys

#Main menu function, asks if user wants to interact.
#Also calls the dice roll function down below.
def menu():
    print ("===Dice Program===")
    print ("Roll dice? y/n")
    Input = input(">>>")

    #If answer is yes then perform dice roll function.
    if Input in ['y', 'Y']:
        diceRoll()

    #If no then quit program.
    elif Input in ['n', 'N']:
        sys.exit()

    #Anything else will report back as invalid.
    else:
        print ("Wrong command!")


#Dice roll function.
#Initialises dice value as 0 then randomises it.
#Then it prints the value to the screen.
def diceRoll():
    diceNum = 0
    diceNum = random.randint(1, 6)
    print ("Dice Value:",diceNum)

#Main program loop that calls the main menu function.
running = True
while running:
    menu()
