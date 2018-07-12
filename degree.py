# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 14:31:02 2018

@author: Emi Ntori
"""

from tkinter import *#to import tkinter library
import tkinter.messagebox# to import messagemox from tkinter library
       
root= Tk()
root.title('Temp. converter')#title
root.geometry("400x200")# the frame size 

def temp():#function created to conduct numeric calculations
    inputValue=int(textBox.get("1.0","end-1c"))# input gotten from the text box and converted to integer for calculations
    value= var.get()
    if value==1:#degree
        degr=(inputValue*(9/5)-32)
        selection = "Your input to Degree celius is: " + str(degr)
        label.config(text = selection)
    elif value==2:#fahrenheit
        fahr=(inputValue*(9/5)+32)
        selection = "Your input to Fahrenheit is:  " + str(fahr)
        label.config(text = selection)
    else:
        tkinter.messagebox.showwarning('Warning','You have to choose an option')
#warning for validation of the radio buttons.a button has to be checked for the conversion to take place
#label was used instead of textbox because it is simpler and time was running out 

choice =Label(root, text="Hello there! Please choose temperature type :")
choice.pack()
var = IntVar()
# variable created to store the option and when one radio button clicked, the value is sent to the temp function
R1 = Radiobutton(root, text="Degree", variable=var, value=1)
R1.pack( anchor = W)#use of anchor to align the widgets
R2 = Radiobutton(root, text="Fahrenheit", variable=var, value=2)
R2.pack( anchor = W )

userLabel = Label(root, text="Enter temperature to be converted :")
userLabel.pack()
textBox=Text(root, height=1, width=15)
textBox.pack()

convertBtn= Button(root, height=1, width=10, text="Convert",command=lambda: temp())
#the command lambda does not take any arguments at all
convertBtn.pack(side=LEFT)
exitBtn= Button(root, height=1, width=10, text="Exit", command= root.destroy)
exitBtn.pack(side=RIGHT)
#the command root.destroy is used to close the tkinter frame/window
 
label = Label(root)#used to display the label to show the results of the conversion
label.pack()
#widgets are packed to be able to be displayed in the tkinter frame    
root.mainloop()