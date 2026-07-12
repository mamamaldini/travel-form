import tkinter as tk
from tkinter import *
from datetime import datetime

root = tk.Tk()
root.title("MamaMaldini Tour & Travels")
root.geometry("700x700")
root.configure(bg="#EAF4FC")
root.resizable(False, False)

title = tk.Label(root, text="MamaMaldini Tour & Travels", font=("Arial", 22, "bold"), bg="#0B3D91", fg="white", pady=15)
title.pack(fill="x")

frame = tk.Frame(root, bg="white", padx=20, pady=20)
frame.pack(pady=20)

# Variables
name = tk.StringVar()
phone = tk.StringVar()
destination = tk.StringVar()
gender = tk.StringVar()
payment = tk.StringVar()
date = tk.StringVar()
passengers = tk.StringVar()
seat = tk.StringVar()
bus = tk.StringVar()
food = tk.IntVar()

# Labels and Entries

fields = [("Full Name", name), ("Phone Number", phone), ("Destination", destination), ("Journey Date (DD/MM/YYYY)", date), ("Passengers", passengers)]

for i, (label, var) in enumerate(fields):
    tk.Label(frame, text=label, font=("Arial", 11), bg="white").grid(row=i, column=0, sticky="w", pady=8)
    tk.Entry(frame, textvariable=var, width=30).grid(row=i, column=1)

# Gender
tk.Label(frame, text="Gender", bg="white", font=("Arial",11)).grid(row=5,column=0,sticky="w")
gender_box = ttk.Combobox(frame,textvariable=gender,width=27,state="readonly")
gender_box["values"]=("Male","Female","Other")
gender_box.grid(row=5,column=1)

# Payment
tk.Label(frame,text="Payment Method",bg="white",font=("Arial",11)).grid(row=6,column=0,sticky="w")
payment_box=ttk.Combobox(frame,textvariable=payment,width=27,state="readonly")
payment_box["values"]=("Cash","Credit Card","Debit Card","UPI","Net Banking")
payment_box.grid(row=6,column=1)

# Seat Preference
tk.Label(frame,text="Seat Preference",bg="white",font=("Arial",11)).grid(row=7,column=0,sticky="w")
seat_box=ttk.Combobox(frame,textvariable=seat,width=27,state="readonly")
seat_box["values"]=("Window","Middle","Aisle")
seat_box.grid(row=7,column=1)

# Bus Type
tk.Label(frame,text="Bus Type",bg="white",font=("Arial",11)).grid(row=8,column=0,sticky="w")

bus_frame=tk.Frame(frame,bg="white")
bus_frame.grid(row=8,column=1,sticky="w")

tk.Radiobutton(bus_frame,text="AC",variable=bus,value="AC",bg="white").pack(side="left")
tk.Radiobutton(bus_frame,text="Non-AC",variable=bus,value="Non-AC",bg="white").pack(side="left")

# Food
tk.Checkbutton(frame, text="Include Food Service", variable=food, bg="white").grid(row=9,column=1,sticky="w",pady=10)

# Submit Function
def submit():
    if name.get()=="" or phone.get()=="" or destination.get()=="":
        messagebox.showerror("Error","Please fill all required fields.")
        return

    data = f"""
Booking Time : {datetime.now()}
Name : {name.get()}
Phone : {phone.get()}
Destination : {destination.get()}
Journey Date : {date.get()}
Passengers : {passengers.get()}
Gender : {gender.get()}
Payment : {payment.get()}
Seat : {seat.get()}
Bus : {bus.get()}
Food Service : {'Yes' if food.get() else 'No'}
-------------------------------------------------------
"""

    with open("Bookings.txt","a") as f:
        f.write(data)

    messagebox.showinfo("Success","Booking Submitted Successfully!")

    clear()

def clear():
    name.set("")
    phone.set("")
    destination.set("")
    gender.set("")
    payment.set("")
    date.set("")
    passengers.set("")
    seat.set("")
    bus.set("")
    food.set(0)

button_frame=tk.Frame(root,bg="#EAF4FC")
button_frame.pack()

tk.Button(button_frame, text="Submit Booking", bg="#28A745", fg="white", font=("Arial",11,"bold"), command=submit, width=18).grid(row=0,column=0,padx=10)

tk.Button(button_frame, text="Clear Form", bg="#DC3545", fg="white", font=("Arial",11,"bold"), command=clear, width=18).grid(row=0,column=1,padx=10)

root.mainloop()
