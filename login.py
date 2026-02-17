import tkinter as tk
import check_for_user 
import transactions

def deposit():
    transactions.deposit(ent1.get())

def withdraw():
    transactions.withdraw(ent1.get())

def balance():
    lbl4.config(text=val)

def check():
    global val 

    val=check_for_user.check(ent1.get(),ent2.get())
    if val!="":
        #changing the configs to provide a better UI to the users
        ent1.config(state="readonly")
        ent2.config(state="readonly")
        lbl3.config(text="Account Verified please proceed")
        btn0.config(state="disabled")
        btn1.config(state="active")
        btn2.config(state="active")
        btn3.config(state="active")
    
    else:
        lbl3.config(text="User not found or incorrect pin entered")
    
def log_in():
    #declaring globals
    global ent1
    global ent2
    global lbl3
    global btn0
    global btn1
    global btn2
    global btn3
    global lbl4

    page4=tk.Tk()

    frame1=tk.Frame(page4)
    frame2=tk.Frame(page4)

    #1st frame
    lbl1=tk.Label(frame1,text="Enter your name")
    lbl1.grid(row=0,column=0)

    ent1=tk.Entry(frame1)
    ent1.grid(row=0,column=1)

    lbl2=tk.Label(frame1,text="Enter your pin")
    lbl2.grid(row=1,column=0)

    ent2=tk.Entry(frame1)
    ent2.grid(row=1,column=1)

    #2nd frame
    btn0=tk.Button(frame2,text="Verify",command=check)
    btn0.pack()

    lbl3=tk.Label(frame2,text="")
    lbl3.pack()

    btn1=tk.Button(frame2,text="View your balance",command=balance,state="disabled")
    btn1.pack()

    lbl4=tk.Label(frame2,text="")
    lbl4.pack()

    btn2=tk.Button(frame2,text="Press to deposit money",command=deposit,state="disabled")
    btn2.pack()

    btn3=tk.Button(frame2,text="Press to withdraw money",command=withdraw,state="disabled")
    btn3.pack()

    frame1.pack(pady=10)
    frame2.pack(pady=10)

    page4.mainloop()
