#Simple notes maker in Python by Caleb/LebbyFoxx.
#Some features may be buggy, so beware!
#Uses files for reading and writing, lists and functions!

#If you want to load a file at any point, don't add anything to the list!
#It will well and truly overwrite the file!
#To add to the file, load it first.

#Make sure the file is in the same directory for it to load!

import os

#The list that will hold the notes.
notes = []

#Main menu function that shows your options.
def mainMenu():
    print("")
    print ("===List Maker CLI===\n")
    print ("What would you like to do?")
    print ("1. Show List.")
    print ("2. Add item.")
    print ("3. Save list.")
    print ("4. Read list.\n")


#Function that shows the list.
def showList():
    
    print("")
    print("-----LIST-----\n")
    #Prints the list vertically, it is neater that way.
    print (*notes, sep='\n')

#Function that adds an item to the 'notes' list.
def addItem():
    addon = input("Add Note: ")
    notes.append(addon)

#Function for saving to file.
def saveFile():
    newFile = input ("File name?: ")
    #If file exists then overwrite, if not then create new file.
    if os.path.exists(newFile + '.txt'):
        print ("")
        print ("WARNING!!!")
        print ("This will overwrite the file. Continue? [y,n]\n")
        yesNo = input("Y/N?>>>")
        if yesNo in ['y', 'Y']:
            with open(newFile + '.txt', 'w') as file:
                #Saves list inside a text file vertically.
                #WILL OVERWRITE THE FILE!!!
                for listitem in notes:
                    file.write('%s\n' % listitem)
        elif yesNo in ['n', 'N']:
            print ("Stopping save...")
            
            mainMenu()
    else:
        with open(newFile + '.txt', 'x') as file:
            for listitem in notes:
                file.write('%s\n' % listitem)

#Reads the file.
def openFile():
    openName = input ("File name?: ")
    global fileOpen
    #See if file exists.
    try:
        fileOpen = open(openName + '.txt')
    except:
        print ("File not found.")
    
    
#Main program loop.
running = True
while running:

    mainMenu()
    Input = int(input("Enter>>>"))

    #Check input and execute functions.
    if Input in [1]:
        try:
            #Open file if loaded? Not sure if this works fully.
            #If not then show current list.
            print(fileOpen.read())
            fileOpen.close()
        except:
            showList()

    if Input in [2]:
        addItem()

    if Input in [3]:
        saveFile()

    if Input in [4]:
        openFile()





