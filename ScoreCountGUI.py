#Simple Score counter program made with Tkinter.
#Press the button(s) to increase the score for each player.

#Written by Caleb Phillips (LebbyFoxx).
#Saturday 24th October 2020.

from tkinter import*

#Window properties.
root = Tk()
root.resizable(False,False)
root.geometry("480x240")
root.title("ScoreCountGUI")

#Player 1 and 2's initial scores.
p1Score = 0
p2Score = 0

#'Score' label above the player scores.
scoreLabel = Label(root,text="Scores", font=("Impact",36))
scoreLabel.place(x=165,y=10)

#Labels displaying the scores.
p1Label = Label(root,text=p1Score,fg="blue", font=("Impact",32))
p1Label.place(x=80,y=60)

p2Label = Label(root,text=p2Score,fg="red", font=("Impact",32))
p2Label.place(x=360,y=60)

#Functions that increase the score at the press of a button.
#Separate functions for both scores.
def increase1():
    global p1Score
    p1Score+=1
    p1Label.configure(text=p1Score)

def increase2():
    global p2Score
    p2Score+=1
    p2Label.configure(text=p2Score)

#Buttons that allow user(s) to increase their score.
btn1 = Button(root, text="Add 1 to Player 1", command=increase1)
btn1.place(x=45,y=150)

btn2 = Button(root, text="Add 1 to Player 2", command=increase2)
btn2.place(x=325,y=150)

#Tkinter program mainloop.
root.mainloop()
