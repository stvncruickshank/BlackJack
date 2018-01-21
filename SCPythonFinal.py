#Steven Cruickshank
#OOPL final project Python
#BlackJack simulator
#
#This program will simulate a game of blackjack. The user is dealt two cards with the option 
#to keep playing if their value is below 21. once the user reaches 21 they in! if they go
#over 21, they lose, and are offered another game. Cash is won or lost depending on if the user
#wins or loses. 
#
#
#While admittedly its a little clunky, All requirements and features appear to be present.
########################3
############################


import random
from tkinter import *
import tkinter.messagebox

cardNum = 0
total = 0
cash = 1000

#lists for card vals
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

root = Tk()

#a little clunky, but all widgets, and variables are set below

sVar = StringVar()
sVar2 = StringVar()
sVar3 = StringVar()
sVar4 = StringVar()
sVar5 = StringVar()
sVar6 = StringVar()
sVal = IntVar()
sVal2 = IntVar()
sVal3 = IntVar()
sVal4 = IntVar()
sVal5 = IntVar()
sVal6 = IntVar()


lbl_temp = Label(root, text="Card Num: 1" + str(""))
lbl_val = Label(root, textvariable=sVar)
lbl_val.config(background="light pink")
lbl_temp.config(background="light pink")

lbl_temp2 = Label(root, text="Card Num: 2" + str(""))
lbl_val2 = Label(root, textvariable=sVar2)
lbl_val2.config(background="light pink")
lbl_temp2.config(background="light pink")

lbl_temp3 = Label(root, text="Card Num: 3" + str(""))
lbl_val3 = Label(root, textvariable=sVar3)
lbl_val3.config(background="light pink")
lbl_temp3.config(background="light pink")

lbl_temp4 = Label(root, text="Card Num: 4" + str(""))
lbl_val4 = Label(root, textvariable=sVar4)
lbl_val4.config(background="light pink")
lbl_temp4.config(background="light pink")

lbl_temp5 = Label(root, text="Card Num: 5" + str(""))
lbl_val5 = Label(root, textvariable=sVar5)
lbl_val5.config(background="light pink")
lbl_temp5.config(background="light pink")

lbl_temp6 = Label(root, text="Card Num: 6" + str(""))
lbl_val6 = Label(root, textvariable=sVar6)
lbl_val6.config(background="light pink")
lbl_temp6.config(background="light pink")

#here are the function definitions
#If the user decides to quit, they're offered a dialog to make sure
def leave():
    result = tkinter.messagebox.askquestion("Quit?", "Are You Sure?", icon='warning')
    if result == 'yes':
        root.quit()

#When the user wins/loses, or starts a new game. This method is called, and will
#hide the widgets until they are needed next game.        
def clear():
    global total
    global cardNum
    btn_hit.config(state="active")
    card_val.config(text="")
    total = 0
    cardNum = 0
    lbl_temp6.pack_forget()
    lbl_val6.pack_forget()
    lbl_temp5.pack_forget()
    lbl_val5.pack_forget()
    lbl_temp4.pack_forget()
    lbl_val4.pack_forget()
    lbl_temp3.pack_forget()
    lbl_val3.pack_forget()
    lbl_temp2.pack_forget()
    lbl_val2.pack_forget()
    lbl_temp.pack_forget()
    lbl_val.pack_forget()

#simple messagebox which displays funds
def showFunds():
    tkinter.messagebox.showinfo("Your Current Funds", "Current funds: $" + str(cash))

#simple message box which asks if you want to reset funds. if you answer yes, your cash is reset
#to $1000
def resetFunds():
    global cash
    result = tkinter.messagebox.askyesno("Are you sure?", "Are you sure you want to reset your funds?")
    if result == True:
        cash = 1000.00

#a simple function which checks to see the card total at the end of each card dealt. 
#if its over 21, the deal button is disabled, and the user is informed they LOSE
def checkVal():
    global cash
    if total > 21:
        btn_hit.config(state="disabled")
        cash -= 50
        result = tkinter.messagebox.askyesno("YOU LOSE!", "You went over 21. New Game?", icon="warning")
        if result == True:
            clear()
            DealCard()
        else:
            clear()

#a HUGE series of if blocks which sort each card/value, as well as control each widget
#based on the card count
def DealCard():
    global cardNum
    global total
    total2 = 0
    cardNum +=1
    if total < 21:
        if cardNum == 1:
            lbl_temp.pack(pady=10)
            lbl_val.pack()
            lbl_temp2.pack(pady=10)
            lbl_val2.pack()
            tempCard = random.choice(cards)
            tempCard2 = random.choice(cards)
            if tempCard.isnumeric() == False and tempCard is not "A":
                total+= 10
            elif tempCard.isnumeric() == False and tempCard is "A":
                if total <=10:
                    total+=11
                else:
                    total+=1
            else:
                total+=int(tempCard)
            if tempCard2.isnumeric() == False and tempCard2 is not "A":
                total2+= 10
            elif tempCard2.isnumeric() == False and tempCard2 is "A":
                if total <=10:
                    total2+=11
                else:
                    total2+=1
            else:
                total2+=int(tempCard2)
            tempSuit = random.choice(suits)
            tempSuit2 = random.choice(suits)
            temp = tempCard + " of " + tempSuit
            temp2 = tempCard2 + " of " + tempSuit2
            total += total2 
            card_val.config(text=str(total))
            sVal.set(total)
            sVal2.set(total2)
            sVar.set(temp)
            sVar2.set(temp2)
            checkVal()
        if cardNum == 2:
            lbl_temp3.pack(pady=10)
            lbl_val3.pack()
            tempCard = random.choice(cards)
            if tempCard.isnumeric() == False and tempCard is not "A":
                total+= 10
            elif tempCard.isnumeric() == False and tempCard is "A":
                if total <=10:
                    total+=11
                else:
                    total+=1
            else:
                total+=int(tempCard)
            tempSuit = random.choice(suits)
            temp = tempCard + " of " + tempSuit
            card_val.config(text=str(total)) 

            sVal3.set(total)
            sVar3.set(temp)
            checkVal()
        if cardNum == 3:
            lbl_temp4.pack(pady=10)
            lbl_val4.pack()
            tempCard = random.choice(cards)
            if tempCard.isnumeric() == False and tempCard is not "A":
                total+= 10
            elif tempCard.isnumeric() == False and tempCard is "A":
                if total <=10:
                    total+=11
                else:
                    total+=1
            else:
                total+=int(tempCard)
            tempSuit = random.choice(suits)
            temp = tempCard + " of " + tempSuit
            card_val.config(text=str(total)) 
            sVal4.set(total)
            sVar4.set(temp)
            checkVal()
        if cardNum == 4:
            lbl_temp5.pack(pady=10)
            lbl_val5.pack()
            tempCard = random.choice(cards)
            if tempCard.isnumeric() == False and tempCard is not "A":
                total+= 10
            elif tempCard.isnumeric() == False and tempCard is "A":
                if total <=10:
                    total+=11
                else:
                    total+=1
            else:
                total+=int(tempCard)
            tempSuit = random.choice(suits)
            temp = tempCard + " of " + tempSuit
            card_val.config(text=str(total)) 
            sVal5.set(total)
            sVar5.set(temp)
            checkVal()
        if cardNum == 5:
            lbl_temp6.pack(pady=10)
            lbl_val6.pack()
            tempCard = random.choice(cards)
            if tempCard.isnumeric() == False and tempCard is not "A":
                total+= 10
            elif tempCard.isnumeric() == False and tempCard is "A":
                if total <=10:
                    total+=11
                else:
                    total+=1
            else:
                total+=int(tempCard)
            tempSuit = random.choice(suits)
            temp = tempCard + " of " + tempSuit
            card_val.config(text=str(total)) 
            sVal6.set(total)
            sVar6.set(temp)
            checkVal()    
    if total == 21:
        global cash
        tkinter.messagebox.showinfo("You win!", "You hit 21! You win!")
        cash+=100
        btn_hit.config(state="disabled")
        clear()        
    if total > 21:
        btn_hit.config(state="disabled")      


 
#menu bar will allow the user to select options from a traditional File menu bar.

menubar = Menu(root)
# display the menu
root.config(menu=menubar, background="light pink")
root.title("Blackjack")
root.resizable(width=False, height=False)
root.geometry("200x500")
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New Game", command=clear)
filemenu.add_command(label="Deal!", command=DealCard)
filemenu.add_command(label="Show Funds", command=showFunds)
filemenu.add_command(label="Reset Funds", command=resetFunds)
filemenu.add_command(label="Quit", command=leave)
menubar.add_cascade(label="File", menu=filemenu)

#labels that are permanantly affixed to the window.
#lots of configurations to alter colors
bj_lbl = Label(root, text="BlackJack", font=("Helvetica", 20))
bj_lbl.configure(foreground="white", background="light pink")
card_total = Label(root, text="Score: ")
card_total.config(background="light pink")
card_val = Label(root, text="Card Total")
card_val.config(background="light pink")
bj_lbl.pack(pady=10)

card_total.pack(pady=10)
card_val.pack()

#this is the button where the user selects "Deal!"
btn_hit = Button(root, text="Deal!", command=DealCard)
btn_hit.pack(pady=10)
btn_hit.config(background="light pink")

root.mainloop()



























