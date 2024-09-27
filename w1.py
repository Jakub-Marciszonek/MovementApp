##### Imports #####

import sys
import datetime
import random
import string

##### Def #####

def QuitCheck(inp):
    if inp.lower() == "quit":
        sys.exit()

##### Login Variables #####

print("Hello user, welcome to the Motion Detector! Let's start.\n\
type quit whenever you would like to end the session.")### user input:

UserRights = ["Admin", "Super-user", "User"]
Name = str(input("What's ur name? "))###name and birthday
QuitCheck(Name)
LName = str(input("What;s ur lastname? "))
QuitCheck(LName)
BDate = input("When you've been born write? \
The date in (dd/mm/yyyy) format. \n")
QuitCheck(BDate)
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
    print(f"------Welcome {Name}, you have {UserRights[0]} rights------")
    CurrentRights = UserRights[0]
elif (Name.lower() == "mira") and (LName.lower() == "vorne") \
and (BDate == "11/11/1111"):
    print(f"======Welcome {Name}, you have {UserRights[1]} rights======")
    CurrentRights = {UserRights[1]}
elif Age >= 18:
    print(f"Welcome {Name}, you have viewer rights.")
    CurrentRights = UserRights[2]
else:
    print(f"Greetings {Name}, you are too young to operate this program. Continue")

print(Name[:2] + LName[:3] + BYear + BMonth + BDay)###username

### Password generator
PasswordSub = str()

while PasswordSub.lower() != "yes" or "y":
    length = int(input("Enter length of the password: "))
    print("Choose characters that are going to be used in password:\n\
1. Digits\n2. Lowercase letters\n3. Uppercase letters\n\
4. Special characters\n5. Generate")
    CharacterList = ""

    while True:
        CharacterChoice = int(input("Pick a number "))
        if (CharacterChoice == 1):
            CharacterList += string.digits
        elif (CharacterChoice == 2):
            CharacterList += string.ascii_lowercase
        elif (CharacterChoice == 3):
            CharacterList += string.ascii_uppercase
        elif (CharacterChoice == 4):
            CharacterList += string.punctuation
        elif (CharacterChoice == 5):
            break
        else:
            print("Invalid data")
        
    Password = []
    for i in range(length):

        PasswordCharacters = random.choice(CharacterList)

        Password.append(PasswordCharacters)

    print(f"The random password is \"{"".join(Password)}\"")
    PasswordSub = str(input("Do you want to submit the password or generate another one?\n\
    (Submit/Generate): "))
    if PasswordSub.lower() == "submit":
        break
    elif PasswordSub.lower() == "generate":
        continue
    else:
        print("Invalid data\nRestarting the generator")
        continue

##### Movement detection #####
### test version with random input
YesNo = ("yes", "no")
Movement = random.choice(YesNo)
#Movement = input("There was a movement in the room? (y/n) \n")
#QuitCheck(Movement)
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
QuitCheck(TemD)
if TemD == "1":###Celsius to Fahrenheit converter
    CDegrees = float(input("Enter the Celsius degrees: "))
    QuitCheck(CDegrees)
    FDegrees = round((CDegrees * 1.8 + 32), 2)
    print(f"The given temperature {CDegrees}C° is {FDegrees}F°")
elif TemD == "2":
    FDegrees = float(input("Enter the Fahrenheit degrees: "))
    QuitCheck(FDegrees)
    CDegrees = round(((FDegrees - 32) / 1.8), 2)
    print(f"The given temperature {FDegrees}F° is {CDegrees}C°")
else:
    print("Invalid data")

# CDegrees = random.randint(20, 100) ###temp tester

if CDegrees <= 40:
    print("CPU is dead cold")
elif CDegrees > 80:
    print("[*]RIP CPU [*]")
elif CDegrees > 65:
    print("It's getting hot here ( ͡° ͜ʖ ͡°)")
else:
    print("ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧")

