import tkinter as tk
import re
import addfunds

def funding():
    addfunds.finance(name,mail,password)

def check():
    global name
    global mail
    global password

    ent1.config(state="readonly")
    ent2.config(state="readonly")
    ent3.config(state="readonly")

    p1=r'^[A-Z]{1}[a-z]+ [A-Z]{1}[a-z]+$'
    p2=r'^[a-zA-Z0-9]{5,}@[a-zA-Z]{3,}\.[a-zA-Z]{2,}'
    
    name=ent1.get()
    mail=ent2.get()
    password=ent3.get()

    temp=name.split()
    temp2=temp[0]

    #checking for validations 
    if not re.fullmatch(p1,name):
        outro.config(text="Invalid Username")

    elif not re.fullmatch(p2,mail):
        outro.config(text="Invalid mail")

    elif temp2 in password or temp2.lower() in password:
        outro.config(text="Do not include your name in the password")

    elif re.fullmatch(p1,name) and re.fullmatch(p2,mail):
        if temp2 not in password and temp2.lower() not in password:
            outro.config(text="You may now add funds to this account")
            btn.config(state="disabled")
            addf.config(state="active")


def sign_in():
    #declaring globals
    global ent1
    global ent2
    global ent3
    global outro
    global btn 
    global addf

    page2=tk.Tk()
    
    frame1=tk.Frame(page2)
    frame2=tk.Frame(page2)
    frame3=tk.Frame(page2)
    #1st frame
    heading=tk.Label(frame1,text="SIGN IN FORM")
    heading.pack()
    
    #2nd frame
    #formatting the entries
    msg1=tk.Label(frame2,text="Enter your full name")
    msg1.grid(row=0,column=0)

    msg2=tk.Label(frame2,text="Enter your email")
    msg2.grid(row=1,column=0)

    msg3=tk.Label(frame2,text="Enter your password")
    msg3.grid(row=2,column=0)

    ent1=tk.Entry(frame2)
    ent1.grid(row=0,column=1)

    ent2=tk.Entry(frame2)
    ent2.grid(row=1,column=1)

    ent3=tk.Entry(frame2)
    ent3.grid(row=2,column=1)

    #3rd frame
    btn=tk.Button(frame3,text="Submit",command=check)
    btn.pack()

    outro=tk.Label(frame3,text="")
    outro.pack()

    addf=tk.Button(frame3,text="Add funds to the account",command=funding,state="disabled")
    addf.pack()

    frame1.pack(pady=10)
    frame2.pack(pady=10)
    frame3.pack(pady=10)

    page2.mainloop()