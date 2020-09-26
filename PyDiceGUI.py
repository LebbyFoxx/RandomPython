#Simple dice rolling GUI program
#Click the button to change the number.

#Written by Caleb Phillips (LebbyFoxx).
#Saturday 26th September 2020.

import random
from tkinter import *

#Dice number variable starts at 0.
diceNum = 0

#Window setup for Tkinter.
root = Tk()
root.resizable(False, False)
root.geometry("240x240")
root.title("PyDice")

#Label above number that says 'Dice.'
diceLabel = Label(root, text="Dice", font=("Helvetica", 20))
diceLabel.place(x=85,y=40)

#The dice number label. This displays your number.
diceNumber = Label(root, text=diceNum, font=("Helvetica", 30))
diceNumber.place(x=100,y=90)

#Function that allows for rolls and re-rolls of the dice.
def diceRoll():
    global diceNum
    diceNum = random.randint(1,6)
    diceNumber.config(text=diceNum)

#Button that utilises the function to roll dice.
btn = Button(root, text="Roll Dice", command=diceRoll)
btn.place(x=86,y=160)

#Mainloop.
root.mainloop()
