import signin
import login
import tkinter as tk
import time

#just for greeting
greeting="evening"
ct=int(time.strftime("%H"))
if ct>=5 and ct<12:
    greeting="morning"
if ct>=12 and ct<=16:
    greeting="afternoon"
if ct>16:
    greeting="evening"

#main formatting
page=tk.Tk()

heading=tk.Label(page,text=f"Good {greeting}",pady=10)
heading.pack()

btn1=tk.Button(page,text="Create an account",command=signin.sign_in).pack()
btn2=tk.Button(page,text="Already have an account",command=login.log_in).pack()

page.mainloop()