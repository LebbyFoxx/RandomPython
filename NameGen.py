#A very simple name generator that uses functions (or 1 function in this case).

#Important module to randomise names.
import random

#Collection of names that will be randomised.
namesMale = ["Kevin", "Roger", "Joe", "Brad", "Ralph", "Chad", "Matt",
             "George", "Steven", "Cliff", "Zach"]

namesFemale = ["Martha", "Kelly", "Zoe", "Chelsea", "April", "Shelly",
               "Leila", "Sally", "Cindy", "Marie"]

surnames = ["Kevinson", "Bradway", "Helfeld", "Wallace", "Milland",
            "Smith", "Biffson", "Broker", "Bolding"]

#Random number determines gender.
maleFemale = [1, 0]

def nameMake():
    rd_maleFemale = random.choice(maleFemale)
    print ("Your name is: ")

    #If number is 1/male then make a male name.
    if rd_maleFemale == 1:
        #This code randomly chooses a name and prints it.
        rd_namesMale = random.choice(namesMale)
        print (rd_namesMale)
        rd_surnames = random.choice(surnames)
        print (rd_surnames)
        print ("Another? y/n")

    #Otherwise make a female one.    
    else:
        #Same as male code but with female names.
        rd_namesFemale = random.choice(namesFemale)
        print (rd_namesFemale)
        rd_surnames = random.choice(surnames)
        print (rd_surnames)
        print ("Another? y/n")

        

print ("Hello! Would you like a name? y/n")
#Program loop.
running = True

while running:
    #User input.
    Input = input(">>>")
    #This capitalises the input. Makes it less 'case-sensitive.'
    Input2 = Input.upper()
    #If the user types 'y' then names are printed.
    if Input2 in ["Y"]:
        nameMake()
    #If 'n' is typed then the program quits.
    elif Input2 in ["N"]:
        print ("Bye!")
        break
    #Anything else will not work.
    #It will loop back around until a valid response has been given.
    else:
        print ("Invalid input.")
    
