#Word generator GUI version using Tkinter.
#Displays three words on the GUI screen.
#Click each button to change either the top, middle or bottom word.
#Add your own words and see what words get generated!

#Written by Caleb Phillips (LebbyFoxx).
#Friday 23rd October 2020.

import random
from tkinter import *

#Randomly generated words.
guiWords = ["Flight", "Sneak", "Grab", "Drink", "Purple", "Robot", "Walking",
            "Scuba", "Truck", "Sauce", "Place", "With", "Mage", "Box",
            "Boxer", "Funny", "Wacky", "Crammed", "Scared", "Happy", "Free",
            "Emotional", "Book", "Chair", "Game", "Insect", "Mammal", "Hello",
            "Cable", "Water", "Chain", "Phone", "Coat", "Table", "Having",
            "Swimming", "Crawling", "Looking", "Thinking", "Small", "Tree",
            "Berry", "Light", "Cottage", "Bottle", "Red", "Orange"]

#Global random word variable that lets us access and change it in functions.
global ran_word

#Initial value of variable.
#All words on startup will be the same random word.
#Pressing the buttons will change this.
ran_word = random.choice(guiWords)

#Window values.
root = Tk()
root.resizable(False,False)
root.geometry("480x240")
root.title("WordGenGUI")

#The label above the random words.
titleLabel = Label(root, text="Random Words:", font=("Impact", 20,))
titleLabel.place(x=150,y=0)

#The three random words.
wordLabel = Label(root, text=ran_word, font=("Helvetica", 18))
wordLabel.place(x=200,y=40)

wordLabel2 = Label(root, text=ran_word, font=("Helvetica", 18))
wordLabel2.place(x=200,y=80)

wordLabel3 = Label(root, text=ran_word, font=("Helvetica", 18))
wordLabel3.place(x=200,y=120)

#Function that changes the top word.
#Generates a new random word and updates the first/top random word label.
def wordGen():
    ran_word = random.choice(guiWords)
    wordLabel.config(text=ran_word)

#Changes the middle word.
def wordGenLabel2():
    ran_word = random.choice(guiWords)
    wordLabel2.config(text=ran_word)

#Changes the bottom word.
def wordGenLabel3():
    ran_word = random.choice(guiWords)
    wordLabel3.config(text=ran_word)


#The three buttons that allow us to change each word.
btn = Button(root, text="Change Top", height=2, width =12, command=wordGen)
btn.place(x=30,y=180)

btn2 = Button(root, text="Change Middle", height=2, width =12, command=wordGenLabel2)
btn2.place(x=195,y=180)

btn3 = Button(root, text="Change Bottom", height=2, width =12, command=wordGenLabel3)
btn3.place(x=360,y=180)

#Tkinter GUI main loop.
root.mainloop()
