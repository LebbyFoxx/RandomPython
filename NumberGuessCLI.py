#Number guessing program on the command line.
#Guess the number (between 1 and 10) and see if you are right!

#Written by Caleb Phillips (LebbyFoxx).
#Monday 28th September 2020.

import random

#Function that randomises number.
def numGuess():
    #Variable 'tries' is set to 5 (and will be reduced if the answer is wrong).
    global tries
    tries = 5
    #Set number to a random value between 1 and 10.
    global number
    number = random.randint(1,10)
    print ("I am thinking of a number from 1 to 10.")
    print ("Can you guess it?")

#Function that restarts game.
def restart():
    #Ask player to input a key to restart game.
    #Anything should do (except for 'tab' and stuff like that? See what works).
    reset = input ("Press a key to restart: ")
    tries = 5
    #Call the numGuess game function again.
    numGuess()
    
#Main loop.
numGuess()
running = True
while running:
    
    #Checking to see if the player has any 'tries' left.
    while tries > 0:
        #Checking to see if input was an integer.
        try:
            numIn = int(input("Number>>> "))
            #If the number is guess right then the player wins!
            if numIn == number:
                print ("You guessed it! :)")
                restart()
        
            elif numIn < number:
                print ("Higher.")
                #If they get it wrong then 'tries' gets reduced by 1.
                tries -=1

            elif numIn > number:
                print ("Lower.")
                #Same goes for picking a lower number.
                tries -=1
      
        #If not an integer then tell user to input one.
        #Luckily there is no penalty for a non-number answer.
        except:
            print ("Please input a number.")

    #When 'tries' has been depleted it is game over and the game restarts.
    print ("Game over!")
    restart()


