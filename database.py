import openpyxl as op

filename="users.xlsx"

def upload(n,m,p,b):
    wb=op.load_workbook(filename)
    ws=wb["Info"]

    ws.append([n,int(b),int(p),m])
    wb.save(filename)
