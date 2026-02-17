import database
import tkinter as tk

def verify():


    value=ent1.get()
    if ent2.get()==password and value.isnumeric() and int(value)>0:
        lbl3.config(text="Successfully uploaded the credentials to the database")
        lbl4.config(text="You may now log in to your account")
        btn.config(state="disabled")
        database.upload(fullname,mail,password,value)


        #disabling the entry widgets
        ent1.config(state="readonly")
        ent2.config(state="readonly")
    else:
        lbl3.config(text="Invalid inputs or wrong password")

def finance(n,m,p):
    global password
    global ent2
    global ent1
    global btn
    global lbl3
    global lbl4
    global mail
    global fullname

    fullname=n
    name=n.split()
    mail=m
    password=p
     

    page3=tk.Tk()

    #inputs from user
    lbl0=tk.Label(page3,text=f"Hello {name[0]}")
    lbl0.pack()

    lbl1=tk.Label(page3,text="Enter the funds below to be depoisted")
    lbl1.pack()

    ent1=tk.Entry(page3)
    ent1.pack()

    lbl2=tk.Label(page3,text="Enter your password below")
    lbl2.pack()

    ent2=tk.Entry(page3)
    ent2.pack()

    btn=tk.Button(page3,text="Proceed",command=verify)
    btn.pack()

    lbl3=tk.Label(page3,text="")
    lbl3.pack()

    lbl4=tk.Label(page3,text="")
    lbl4.pack()

    page3.mainloop()
    
