#Simple word length guesser that uses a simple function to guess the length.
#Please note that this program counts special characters and spaces as letters, since it is a simple program.


import random

#Length guesser function.
#Here we use 'len' to guess the length of the input.
def wordLength():
    word = input("Please enter a word! >>> ")
    length = len(word)
    print ("Your word, ", word, " Has ",length, " character(s) in it! Nice!")

#Intial question asking if the user wants to participate.
print ("Welcome to my length guesser! Would you like to enter a word? y/n")

#Program loop.
running = True
while running:

    yesNo = input(">>>")

    #If user says 'Yes' then perform function.
    #We also ask if the user would like to continue with another word.
    if yesNo in ['y', 'Y']:
        wordLength()
        print ("Again? y/n")
        
    #If user says 'No' then say goodbye and break/end program.
    elif yesNo in ['n', 'N']:
        print ("Goodbye!")
        break

    #Anything else won't work.
    else:
        print ("Invalid response!")
    
    
    
