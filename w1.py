##### Imports #####

import sys
import datetime
import random

##### Login Variables #####

print("Hello user, welcome to the Motion Detector! Let's start.")### user input:
Name = str(input("What's ur name? "))###name and birthday
LName = str(input("What;s ur lastname? "))
BDate = input("When you've been born write? \
The date in (dd/mm/yyyy) format. \n")
PDate = datetime.datetime.now()
BDay, BMonth, BYear = map(str, BDate.split("/"))# map is deviding one 
# variable into 3 new ones respectivly by .split function where separator
# is defined as / 

Age = int(PDate.year) - int(BYear)
if (int(BMonth) > int(PDate.month) and int(BDay) > int(PDate.day)):
    Age = Age-1 ###counting age based on birth date

##### Checking login data and creating username #####

if (len(BYear) != 4) or (int(BMonth) < 1 or int(BMonth or len(BMonth) != 2 ) > 12)\
or ((len(BDay) != 2) or (int(BDay) < 1) or (int(BDay) > 31)):
    print("#######Invalid format of date#######")###checking format 

###login
if (Name.lower() == "jakub") and \
(LName.lower() == "marciszonek") and (BDate == "30/01/2004"): 
    print(f"------Welcome {Name}, you have admin rights------")
elif (Name.lower() == "mira") and (LName.lower() == "vorne") \
and (BDate == "11/11/1111"):
    print(f"======Welcome {Name}, you have super-user rights======")
elif Age >= 18:
    print(f"Welcome {Name}, you have viewer rights.")
else:
    print(f"Greetings {Name}, you are too young to operate this program. Continue")

while True:
    print(Name[:2] + LName[:3] + BYear + BMonth + BDay)###username

    ##### Movement detection #####
    ### test version with random input
    YesNo = ("yes", "no")
    Movement = random.choice(YesNo)
    #Movement = input("There was a movement in the room? (y/n) \n")
    if (Movement.lower() == "yes" or Movement.lower() == "y"):
        print("Movement detected")
    elif (Movement.lower() == "no" or Movement.lower() == "n"):
        print("Movement not detected")
    else:
        print("Invalid data")

    ##### Temperature converter and evaluator #####

    print("Celsius to Fahrenheit calculator")

    TemD = (input("Choose the units that you want to convert\
    \n1. Celsius degrees\n2. Fahrenheit degrees\n"))
    # if TemD == "1":###Celsius to Fahrenheit converter
    #     CDegrees = float(input("Enter the Celsius degrees: "))
    #     FDegrees = round((CDegrees * 1.8 + 32), 2)
    #     print(f"The given temperature {CDegrees}C° is {FDegrees}F°")
    # elif TemD == "2":
    #     FDegrees = float(input("Enter the Fahrenheit degrees: "))
    #     CDegrees = round(((FDegrees - 32) / 1.8), 2)
    #     print(f"The given temperature {FDegrees}F° is {CDegrees}C°")
    # else:
    #     print("Invalid data")

    CDegrees = random.randint(20, 100)

    if CDegrees <= 40:
        print("CPU is dead cold")
    elif CDegrees > 80:
        print("[*]RIP CPU [*]")
    elif CDegrees > 65:
        print("It's getting hot here ( ͡° ͜ʖ ͡°)")
    else:
        print("ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧")



    Quit = input("Do you want to quit or restart the programme(quit/restart?) ")

    if Quit.lower() == "quit":
        print("Thanks for visiting. Welcome back soon.")
        break
    elif Quit.lower() == "restart":
        print("Programme restrting")
        pass
    else:
        print("Invalid command\nshutting down the programme")
        break
