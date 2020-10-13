#Random word generator (CLI version).
#Print random words to the console!
#Add some words of your own and see what you get!

#Written by Caleb Phillips (LebbyFoxx).
#Tuesday 13th October 2020.

import random
import sys

#The list of random words.
#Some words may be repeated at the same time. Be aware of that!
#Order of words may not make sense either. Be aware of that too!
words = ["Bacon", "Through", "Wake", "Eat", "Bike", "Round", "Make", "Fight",
         "Break", "Jump", "Herd", "Curdle", "Milk", "Car", "Remote", "Handle",
         "Sweet", "Controller", "Computer", "Table", "Walking", "Swimming",
         "Sand", "Earth", "Add", "Subtract", "With", "Without", "Speaking",
         "Brains", "Wheel", "Adventure", "Space", "Escape", "While", "For",
         "Not", "And", "Flying", "Sneaking", "Cooking", "House", "Lights",
         "Darkness", "Sreet", "Function", "Happy", "Sad", "Interesting",
         "Club", "Sandwich", "Road", "Ride", "Radio", "Mail", "Heap", "Touch",
         "Sledge", "Snow", "Sound", "Grabbing", "Smelling", "Looking"]

#Word generator function.
#Randomises and prints random words.
def wordGenerate():
    #Choose how many words you want randomised and printed.
    inputNum = int(input("How many?: "))
    
    #If inputted number exceeds 6 then it won't print random words.
    #Make the limit larger if you want, or remove it entirely.
    if inputNum > 6:
        print ("\nTOO LARGE!")
        print ("Generator supports 6 words at a time!")
        
    else:
        #Separating the words. Makes printed list look nice.
        print('')
        #Randomly generating words.
        for x in range(inputNum):
            ranWord = random.choice(words)
            print (ranWord)

#Initial 'menu text.'
def menuText():
    print ("\n===Word Generator===")
    print ("1. Generate word(s)")
    print ("2. Quit")

#Call 'menuText' function to represent initial menu.
#Shows the user thier options when starting the program.
menuText()

#Main program loop.
running = True
while running:

    #Ask the user which option from the menu that they want.
    Input = int(input(">>>"))

    #If input is 1 then run word generator function.
    if Input in [1]:
        wordGenerate()
        #Call the 'menuText' function again to reiterate options to the user. 
        menuText()

    #If input is 2 then end program.
    elif Input in [2]:
        sys.exit()

    #Any other number does not work.
    #The program will loop until either 1 or 2 has been inputted.
    #Other characters will or may break the program, INPUT MUST BE A NUMBER!
    else:
        print ("Wrong input!")
