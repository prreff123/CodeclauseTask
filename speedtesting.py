words = ['Asus','Mango','Apple','gun','fan','door','TV','mobile','laptop','Google','facebook','Netflix','Amazon','FAANG','College','school','Hello','No','Yes','Table']

def Labelslider():
    global count,slidewords
    text = 'Welcome To Speed Typing Testing Game'
    if(count>=len(text)):
        count = 0
        slidewords = ''
    slidewords += text[count]
    count += 1   
    fontlabel.configure(text=slidewords)
    fontlabel.after(130,Labelslider)

def time():
    global timeleft,score,miss
    if(timeleft>=11):
        pass
    else:
        timerlabelcount.configure(fg='red')
    if (timeleft>0):
        timeleft -= 1
        timerlabelcount.configure(text=timeleft)
        timerlabelcount.after(1000,time)
    else:
        gameplaydetail.configure(text='Hit = {} | Miss = {} | Total score = {}'.format(score,miss,score-miss))
        rr = messagebox.askretrycancel('Noification','for play again Hit retry buton!')
        if (rr==True):
            score = 0
            timeleft = 60
            miss = 0
            timerlabelcount.configure(text=timeleft)
            wordlabel.configure(text=words[0])
            scorelabelcount.configure(text=score)    

def startgame(event):
    global score,miss
    if (timeleft==60):
        time()

    gameplaydetail.configure(text='')
    if(wordentry.get()==wordlabel['text']):
        score += 1
        scorelabelcount.configure(text=score)
    else:
        miss += 1
    random.shuffle(words)
    wordlabel.configure(text=words[0])        
    wordentry.delete(0,END)

from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.geometry('1000x550+150+60')
root.configure(bg='powder blue')
root.title('Typing Speed Testing Game')
score = 0
timeleft = 60
count = 0
slidewords = ''
miss = 0

fontlabel = Label(root,text='',font=('arial',25,'italic bold'),bg='powder blue',fg='red')
fontlabel.place(x=180,y=10)
Labelslider()

random.shuffle(words)
############################################################################################

wordlabel = Label(root,text=words[0],font=('arial',40,'italic bold'),bg='powder blue')
wordlabel.place(x=400,y=200)

############################################################################################

scorelabel = Label(root,text='Your Score : ',font=('arial',25,'italic bold'),bg='powder blue')
scorelabel.place(x=10,y=100)

scorelabelcount = Label(root,text=score,font=('arial',25,'italic bold'),bg='powder blue',fg='blue')
scorelabelcount.place(x=80,y=150)

############################################################################################

timerlabel = Label(root,text='Time Left : ',font=('arial',25,'italic bold'),bg='powder blue')
timerlabel.place(x=800,y=100)

timerlabelcount = Label(root,text=timeleft,font=('arial',25,'italic bold'),bg='powder blue',fg='blue')
timerlabelcount.place(x=850,y=150)

############################################################################################

gameplaydetail = Label(root,text='Type Word and Hit Enter Button',font=('arial',30,'italic bold'),bg='powder blue',fg='dark grey')
gameplaydetail.place(x=200,y=450)

############################################################################################
wordentry = Entry(root,font=('arial',30,'italic bold'),bd=10,justify='center')
wordentry.place(x=260,y=300)
wordentry.focus_set()
############################################################################################
root.bind('<Return>',startgame)
root.mainloop()