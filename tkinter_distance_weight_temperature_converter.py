"""
File Name: tkinter_unit_converter.py
Author: Richy Nwaehi
Date: 2026-01-16
Description:
    A Tkinter-based graphical user interface (GUI) application that allows users
    to convert between different measurement units including:

    - Distance (Miles ↔ Kilometres)
    - Weight (Kilograms ↔ Grams)
    - Temperature (Celsius ↔ Fahrenheit)

    The application uses multiple windows (Toplevel) and provides
    interactive buttons, entry fields, and text output for conversions.

Technologies Used:
    - Python 3
    - Tkinter (GUI library)

Purpose:
    Personal project to practice GUI programming, event handling,
    and unit conversion logic in Python.
"""



from tkinter import *
import random

tkinter = Tk()
tkinter.title("Conversions")
tkinter.config(background="Black")
tkinter.geometry("375x300")

kilometres = 1.60934
miles = 0.621371
kilo = 1.60
grams = 1000
distance_mode = None
weight_mode = None
                                    #Distance Converter
def MtoK():
    global top,my_entry,box_3,e1,T1,value,number,prompt,distance_mode
    distance_mode = "m-to-k"
    prompt = "1 mile is 1.60934 kilometres."
    my_entry.delete(0,END)
    my_entry.insert(0,prompt)
    Text_3="Enter the number for Miles."
    box_3.delete(0,END)
    box_3.insert(0,Text_3)
    
def KtoM():
    global top,prompt_1,my_entry,box_3,e1, distance_mode
    distance_mode = "k-to-m"
    prompt_1="1 kilometre is 0.621371 miles."
    my_entry.delete(0,END)
    my_entry.insert(0,prompt_1)
    Text_4="Enter the number for Kilometres. "
    box_3.delete(0,END)
    box_3.insert(0,Text_4)
   
def ktom():
    global kilo,e1,Text_3
    T1.delete("1.0", END)
    num = float(e1.get())
    result = num*miles
    T1.insert(0.0, f"{num} kilometres = {result:.3f} miles")
        
def mtok():
    global kilometres,prompt_1,Text_3,e1,my_entry,my_button,button_2,prompt
    
    number = float(e1.get())
    mult = number*kilometres
    T1.insert(0.0,f"{number} miles = {mult:.3f} km")

def submit():
    T1.delete("1.0", END)
    number = float(e1.get())

    if distance_mode == "m-to-k":
        mtok()

    elif distance_mode == "k-to-m":
        ktom()

def Clear():
    e1.delete(0,END)
    T1.delete(0.0,END)
       
    
def Convo():
    global top,my_entry,box_3,e1,T1,value,number,prompt_1,my_button,button_2,prompt
    top= Toplevel()
    top.config(background="Navy Blue")
    top.title("Distance")
    top.geometry("350x300")
    
    my_label = Label(top,text="Choose Your Conversion",fg="black",bg="Orange",font="Courier 10 bold")
    my_label.place(x=85,y=2)

    my_button = Button(top,text="Miles-->Kilometres",fg="orange",bg="blue",font="Courier 10 bold",command=lambda: [MtoK()])
    my_button.place(x=35,y=30)

    button_2 = Button(top,text="Kilometres-->Miles",fg="orange",bg="blue",font="Courier 10 bold",command=lambda: [KtoM()])
    button_2.place(x=185,y=30)

    my_entry = Entry(top,bd=1,font= "Courier 10",width=30)
    my_entry.place(x=65,y=70)

    box_3 = Entry(top,bd=1,font="Courier 10",width=32)
    box_3.place(x=58,y=100)

    l1 = Label(top,text="Enter your number below",fg="black",bg="Orange",font="Courier 10 bold")
    l1.place(x=85,y=125)

    e1 = Entry(top,bd=1,font="Courier 10",width=15)
    e1.place(x=115,y=150)

    buty = Button(top,text="Submit",fg="Blue",bg="Yellow",font="Courier 10 bold",command=submit)
    buty.place(x=146,y=172)

    T1 = Text(top,width=25,height=3)
    T1.place(x=80,y=200)

    D = Button(top, text = "Clear",fg="White",font="Courier 10 bold",bg="Black", command=Clear, width=6)
    D.place(x=146,y=251)

                            #Weight Converter

weight_mode = None

def clear():
    e2.delete(0,END)
    T2.delete(0.0,END)

def KtoG():
    global top_1,My_entry,box_2,prompt_2, weight_mode
    weight_mode = "k-to-g"
    prompt_2="1 Kilogram is 1000grams."
    My_entry.delete(0,END)
    My_entry.insert(0,prompt_2)
    Text_2="Enter the number for Kilograms. "
    box_2.delete(0,END)
    box_2.insert(0,Text_2)

def GtoK():
    global top_1,prompt_3,My_entry,box_2, weight_mode
    weight_mode = "g-to-k"
    prompt_3="1 gram is 0.001 kilograms."
    My_entry.delete(0,END)
    My_entry.insert(0,prompt_3)
    Text_1="Enter the number for grams"
    box_2.delete(0,END)
    box_2.insert(0,Text_1)
    
def ktog():
    global kilo,e1,Text_3
    T2.delete("1.0", END)
    numy = float(e2.get())
    result = numy*1000
    T2.insert(0.0, f"{numy} kilograms = {result:.3f} grams")
        
def gtok():
    global kilo,e1,Text_3
    T2.delete("1.0", END)
    numy = float(e2.get())
    result = numy/1000
    T2.insert(0.0, f"{numy} grams = {result:.3f} kilograms")
    
def submit_1():
    T2.delete("1.0", END)
    number = float(e2.get())

    if weight_mode == "k-to-g":
        ktog()

    elif weight_mode == "g-to-k":
        gtok()
    
def Weight():
    global top_1,My_entry,box_2,e2,T2
    top_1= Toplevel()
    top_1.title("Weight")
    top_1.config(background="Navy Blue")
    top_1.geometry("350x300")

    my_label = Label(top_1,text="Choose Your Conversion",fg="black",bg="Orange",font="Courier 10 bold")
    my_label.place(x=85,y=2)

    my_button = Button(top_1,text="Kilograms-Grams",fg="orange",bg="blue",font="Courier 10 bold",command=lambda: [KtoG()])
    my_button.place(x= 35,y=30)

    button_2 = Button(top_1,text="Grams-Kilograms",fg="orange",bg="blue",font="Courier 10 bold",command=lambda: [GtoK()])
    button_2.place(x=185,y=30)

    My_entry = Entry(top_1,bd=1,font= "Courier 10 ",width=27)
    My_entry.place(x=75,y=70)

    box_2 = Entry(top_1,bd=1,font="Courier 10",width=30)
    box_2.place(x=65,y=100)

    l2 = Label(top_1,text="Enter your number below",fg="black",bg="Orange",font="Courier 10 bold")
    l2.place(x=85,y=125)

    e2 = Entry(top_1,bd=1,font="Courier 10",width=15)
    e2.place(x=115,y=150)

    buty_2 = Button(top_1,text="Submit",fg="Blue",bg="Yellow",font="Courier 10 bold",command=submit_1)
    buty_2.place(x=146,y=172)

    T2 = Text(top_1,width=25,height=3)
    T2.place(x=80,y=200)

    D = Button(top_1, text = "Clear",fg="White",font="Courier 10 bold",bg="Black", command=clear, width=6)
    D.place(x=146,y=251)
    
                            #Temperature Converter
temp_mode = None

def clear():
    e3.delete(0,END)
    T3.delete(0.0,END)
    
def CtoF():
    global top_2,prompt_4,My_entry,my_box, temp_mode
    temp_mode = "c-to-f"
    prompt_4="1 celsius is 33.8Farenheit."
    My_entry.delete(0,END)
    My_entry.insert(0,prompt_4)
    Text="Enter the number for Celsius."
    my_box.delete(0,END)
    my_box.insert(0,Text)

def FtoC():
    global top_2,prompt_4,My_entry,my_box, temp_mode
    temp_mode = "f-to-c"
    prompt_5="1 Farenheit is -17.222 celsius."
    My_entry.delete(0,END)
    My_entry.insert(0,prompt_5)
    prompt_6="Enter the number for Farenheit"
    my_box.delete(0,END)
    my_box.insert(0,prompt_6)

def ctof():
    global kilo,e1,Text_3
    T3.delete("1.0", END)
    numy = float(e3.get())
    result = numy*9/5 + 32
    T3.insert(0.0, f"{numy} °C = {result:.1f} °F")
        
def ftoc():
    global kilo,e1,Text_3
    T3.delete("1.0", END)
    numy = float(e3.get())
    result = (numy-32) * 5/9
    T3.insert(0.0, f"{numy} °F = {result:.1f} °C")
    
def submit_2():
    T3.delete("1.0", END)
    number = float(e3.get())

    if temp_mode == "c-to-f":
        ctof()

    elif temp_mode == "f-to-c":
        ftoc()
    

def Temperature():
    global top_2,My_entry,my_box,e3, T3
    top_2= Toplevel()
    top_2.title("Temperature")
    top_2.config(background="Navy Blue")
    top_2.geometry("350x300")

    my_label = Label(top_2,text="Choose Your Conversion",fg="black",bg="Orange",font="Courier 10 bold")
    my_label.place(x=85,y=2)

    my_button = Button(top_2,text="Celsius-Farenheit",fg="orange",bg="blue",font="Courier 10 bold",command=lambda: [CtoF()])
    my_button.place(x= 35,y=30)

    button_2 = Button(top_2,text="Farenheit-Celsius",fg="orange",bg="blue",font="Courier 10 bold",command=lambda: [FtoC()])
    button_2.place(x=185,y=30)

    My_entry = Entry(top_2,bd=1,font= "Courier 10",width=32)
    My_entry.place(x=58,y=70)

    my_box = Entry(top_2,bd=1,font="Courier 10",width=30)
    my_box.place(x=65,y=100)

    l3 = Label(top_2,text="Enter your number below",fg="black",bg="Orange",font="Courier 10 bold")
    l3.place(x=85,y=125)

    e3 = Entry(top_2,bd=1,font="Courier 10",width=15)
    e3.place(x=115,y=150)

    buty_3 = Button(top_2,text="Submit",fg="Blue",bg="Yellow",font="Courier 10 bold",command=submit_2)
    buty_3.place(x=146,y=172)

    T3 = Text(top_2,width=25,height=3)
    T3.place(x=80,y=200)

    F = Button(top_2, text = "Clear",fg="White",font="Courier 10 bold",bg="Black", command=clear, width=6)
    F.place(x=146,y=251)
    
                #Main Menu
L1 = Label(tkinter,text="What conversion would you like to choose?",relief=SUNKEN,width=38,font="Calibri 12 bold")
L1.place(x=50,y=50)

My_Button = Button(tkinter,text="Distance",fg="blue",font="Courier 10 bold",bg="Yellow",command=Convo)
My_Button.place(x =70,y=78)

My_Button1 = Button(tkinter,text="Weight",fg="blue",font="Courier 10 bold",bg="Yellow",command= Weight)
My_Button1.place(x=70,y=107)

My_Button2 = Button(tkinter,text="Temperature",fg="blue",font="Courier 10  bold",bg="Yellow",command=Temperature)
My_Button2.place(x=70,y=136)

My_Button3 = Button(tkinter,text="Exit",fg="Purple",font="Courier 10 bold",bg="grey", command= exit)
My_Button3.place(x=70,y=162)


