import smtplib
from email.message import EmailMessage

#This segment consists of place holders the programmer needs to enter his/her mail and app password to proceed

def sendmail1(name,mail,money):

    email = EmailMessage()
    email['From'] = "your mail"
    email['To'] = f"{mail}"
    email['Subject'] = "Test Mail"
    email.set_content(f"Hello {name},an amount of {money} has been deposited to your account")
    
    #connecting with the gmail domain and SMTP port 
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("your mail", "your app password")
    server.send_message(email)
    server.quit()

def sendmail2(name,mail,money):

    email = EmailMessage()
    email['From'] = "your mail"
    email['To'] = f"{mail}"
    email['Subject'] = "Test Mail"
    email.set_content(f"Hello {name},an amount of {money} has been withdrawn from your account")
    
    #connecting with the gmail domain and SMTP port
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("your mail", "your app password")
    server.send_message(email)
    server.quit()


