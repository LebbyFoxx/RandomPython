#Very simple CLI Python counter.
#REMEMBER: Doesn't run when computer is in sleep mode!

import time

#Asks how many minutes the user wants to count.
inputCount = int(input("How many minutes?: "))

#Multiplies input by 60 seconds.
SecCount = inputCount * 60

#Important starting variables.
Minutes = 0
Seconds = 0
x = 0

#While x is less than input in 'Seconds' add 1 to x and wait a second.
while (x < SecCount):
    #'x' is the real timer, 'Seconds' is just for display.
    #Printing seconds and minutes is neater than '87 seconds' etc.
    x+=1
    #'Seconds' therefore counts up with 'x', but resets after a minute.
    Seconds+=1
    #Print 'Minutes' and 'Seconds' on screen.
    print ("Minutes:", Minutes, "Seconds:", Seconds)
    time.sleep(1)
    

    #If seconds are equal to or larger than 60...
    #Return 'Seconds' to 0 and add 1 to 'Minutes.'
    if (Seconds >= 60):
        Seconds = 0
        Minutes += 1

#Print 'Done!' when the timer ('x') has finished counting up.
print ("Done!")
        
            

    


        
  
        
