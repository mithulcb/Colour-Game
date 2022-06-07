import matplotlib.pyplot as pl
import tkinter
import random


colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0

#to put 30
timeleft = 10


# function that will start the game.
def startGame(event):
    if timeleft == 10:
        
        countdown()

        
    nextColour()



def nextColour():
   
    global score
    global timeleft


    if timeleft > 0:

        # make the text entry box active.
        e.focus_set()

        # if the colour typed is equal
        # to the colour of the text
        if e.get().lower() == colours[1].lower():
            score += 1

        # clear the text entry box.
        e.delete(0, tkinter.END)

        random.shuffle(colours)

        # change the colour to type, by changing the
        # text _and_ the colour to a random colour value
        label.config(fg=str(colours[1]), text=str(colours[0]))

        # update the score.
        scoreLabel.config(text="Score: " + str(score))

    # Countdown timer function


def countdown():
    global timeleft

   
    if timeleft > 0:
        
        timeleft -= 1

        timeLabel.config(text="Time left: "
                              + str(timeleft))

      
        timeLabel.after(1000, countdown)

  


root = tkinter.Tk()


root.title("COLORGAME")


root.geometry("375x200")


instructions = tkinter.Label(root, text="Type in the colour"
                                        "of the words, and not the word text!",
                             font=('Helvetica', 12))
instructions.pack()


scoreLabel = tkinter.Label(root, text="Press enter to start",
                           font=('Helvetica', 12))
scoreLabel.pack()


timeLabel = tkinter.Label(root, text="Time left: " +
                                     str(timeleft), font=('Helvetica', 12))

timeLabel.pack()


label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()


e = tkinter.Entry(root)


root.bind('<Return>', startGame)
e.pack()

# set focus on the entry box
e.focus_set()
#main
d={}
x=input('enter name')
root.mainloop()
print(score)
t=open('t2.txt','a')
s=open('t1.txt','a')
d[x]=score
t.write(str(d[x])+'\n')
s.write(x+'\n')
t.close()
s.close()

t=open('t1.txt','r')
name=t.readlines()
s=open('t2.txt','r')
score=s.readlines()
l1=[]
l2=[];d={}
print(name)
for i in name:
    z=i.strip('\n')
    l1+=[z]
for i in score:
    z=i.strip('\n')
    l2+=[z]
print(l1,'name')
print(l2,'score')
length=len(l1)
for i in range(length):
    d[l1[i]]=l2[i]
print(d)

pl.yticks([0,1,2,3,4,5])
pl.bar(l1,l2,width=5)
pl.show()