import smtplib
from email.message import EmailMessage

def sendmail1(name,mail,money):
    email = EmailMessage()
    email['From'] = "your mail"
    email['To'] = f"{mail}"
    email['Subject'] = "Test Mail"
    email.set_content(f"Hello {name},an amount of {money} has been deposited to your account")
    
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
    
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("your mail", "your app password")
    server.send_message(email)
    server.quit()

