#This segment is not for the users its for authorized person 

import openpyxl as op
import tkinter as tk

wb = op.load_workbook("users.xlsx")
ws1 = wb["Deposit"]
ws2 = wb["Withdraw"]

depositusers = {}
withdrawusers = {}

for i in range(2, 10):
    if ws1[f"C{i}"].value is None or ws1[f"B{i}"].value is None:
        continue

    if ws1[f"C{i}"].value not in depositusers:
        depositusers[ws1[f"C{i}"].value] = ws1[f"B{i}"].value
    else:
        depositusers[ws1[f"C{i}"].value] += ws1[f"B{i}"].value


for i in range(2, 10):
    if ws2[f"C{i}"].value is None or ws2[f"B{i}"].value is None:
        continue

    if ws2[f"C{i}"].value not in withdrawusers:
        withdrawusers[ws2[f"C{i}"].value] = ws2[f"B{i}"].value
    else:
        withdrawusers[ws2[f"C{i}"].value] += ws2[f"B{i}"].value


#print(depositusers)
#print(withdrawusers)

s1=sorted(depositusers.items(),key=lambda x:x[1],reverse=True)
s2=sorted(withdrawusers.items(),key=lambda x:x[1],reverse=True)

#print(s1)
#print(s2)

#print(highestdeposit)
#print(highestwithdrawer)

output=""
output+="DEPOSITS\n"
for name,money in depositusers.items():
    output+=name+":"+str(money)+"\n"
output+="\n"
output+="WITHDRAW\n"
for name,money in withdrawusers.items():
    output+=name+":"+str(money)+"\n"

output+=f"\nThe maximum deposit made by {s1[0][0]} of rupees {s1[0][1]}\n"
output+=f"\nThe maximum withdraw made by {s2[0][0]} of rupees {s2[0][1]}"


def show():
    text.insert("1.0",output)
    text.config(state="disabled")

page6=tk.Tk()

btn=tk.Button(page6,text="Summarize the transactions",command=show)
btn.pack()

text=tk.Text(page6)
text.pack()

page6.mainloop()
