import tkinter as tk
from tkinter import *


root=Tk()
root.geometry("1000x600")



#text for form
txt=Label(root,text="Welcome to MamaMaldini Tour and Travels",bg="black",fg="white",font=("comicsansms",16,"bold")).grid(row=0,column=12)
username=Label(root,text="Enter Your Username",bg="black",fg="white",font=("comicsansms",10,"bold")).grid(row=5,column=0)
phone=Label(root,text="Enter Your Phone Number",bg="black",fg="white",font=("comicsansms",10,"bold")).grid(row=6,column=0)
destination=Label(root,text="Enter Your Destination",bg="black",fg="white",font=("comicsansms",10,"bold")).grid(row=7,column=0)
gender=Label(root,text="Enter Your Gender",bg="black",fg="white",font=("comicsansms",10,"bold")).grid(row=8,column=0)
payment=Label(root,text="Enter Your Payment Method",bg="black",fg="white",font=("comicsansms",10,"bold")).grid(row=9,column=0)
foodservice=Label(root,text="Food Service",bg="black",fg="white",font=("comicsansms",10,"bold")).grid(row=10,column=0)


#tkinter variables to store the values of the form
usernamevalue=StringVar()
phonevalue=StringVar()
destinationvalue=StringVar()
gendervalue=StringVar() 
paymentvalue=StringVar()
foodservicevalue=IntVar()


#entries and packing of the entries
nameentry=Entry(root,textvariable=usernamevalue,bg="black",fg="white",font=("comicsansms",10,"bold")).grid(row=5,column=3)
phoneentry=Entry(root,textvariable=phonevalue,bg="black",fg="white",font=("comicsansms",10,"bold")).grid(row=6,column=3)
destinationentry=Entry(root,textvariable=destinationvalue,bg="black",fg="white",font=("comicsansms",10,"bold")).grid(row=7,column=3)
genderentry=Entry(root,textvariable=gendervalue,bg="black",fg="white",font=("comicsansms",10,"bold")).grid(row=8,column=3)
paymententry=Entry(root,textvariable=paymentvalue,bg="black",fg="white",font=("comicsansms",10,"bold")).grid(row=9,column=3)

#checkbox for food service
foodservice=Checkbutton(root,text="Want to include food service?",variable=foodservicevalue,bg="black",fg="white",font=("comicsansms",10,"bold")).grid(row=10,column=3)

#button to submit the form
def getvals():
    print("The username is:",usernamevalue.get())
    print("The phone number is:",phonevalue.get())
    print("The destination is:",destinationvalue.get())
    print("The gender is:",gendervalue.get())
    print("The payment method is:",paymentvalue.get())
    print("Food Service:",foodservicevalue.get())

Button(text="Submit",bg="black",fg="white",font=("comicsansms",10,"bold"),command=getvals).grid(row=11,column=3)

root.mainloop()

