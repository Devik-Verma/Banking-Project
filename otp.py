import random
import pywhatkit as kit

def generate(n):
    a=str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
    
    with open("containotp.txt","w") as file:
        file.write(a)
    
    num=f"+91{n}"
    kit.sendwhatmsg_instantly(num,a, wait_time=20, tab_close=True)

    