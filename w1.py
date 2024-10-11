##### Imports #####

import json
import requests
import sys
import datetime
import random
import string

##### User Data Variables  #####

UserRights = "User"
Name = ""
LName = ""
BDate = ""
BDay = ""
BMonth = ""
BYear = ""
PDate = datetime.datetime.now()

##### Password Variables #####

CharacterList = []
CharacterChoice = 0
Length = 0

###List in Use###

NewUser = {}

##### Quit function #####

def QuitCheck(inp):
    if str(inp).lower() == "quit":
        sys.exit()

##### Checkes if somebodies username is already saved #####
def LoginIn(Username, Password):                            
    with open("data/Users.json", "r") as file:
        data = json.load(file)
        for i in range(len(data["Users"])):
            if Username == data["Users"][i]["Login"]:
                LogNr = i
            else:
                LogNr = -1
            if Password == data["Users"][i]["Password"]:
                PassNr = i
            else:
                PassNr = LogNr - 1
            if LogNr == PassNr:
                print("Succsesfully loged in")
                return LogNr
        print("Incorrect Login or Password")
        return -1

def UsernameCheck(Username):
    with open("data/Users.json", "r") as file:
        data = json.load(file)
    for i in range(len(data["Users"])):
        if Username == data["Users"][i]["Login"]:
            print("Username is occupied")
            return True
        else:
            return {"Login":Username}
###### Personale data input ######
def UserData():
    
    global Name, LName, BDate, BDay, BMonth, BYear

    Name = str(input("What's ur name? ")).title()###name and birthday
    QuitCheck(Name)
    LName = str(input("What's ur lastname? ")).title()
    QuitCheck(LName)
    while True:
        BDate = input("When you've been born write? \
The date in (dd/mm/yyyy) format. \n")
        QuitCheck(BDate)
        
        BDay, BMonth, BYear = map(str, BDate.split("/"))# map is deviding one 
        # variable into 3 new ones respectivly by .split function where separator
        # is defined as /  
        if not BDay or not BMonth or not BYear:###not operator work simular as - in math
            print("#######Invalid format of date#######")
        if (len(BYear) != 4) or int(BMonth) < 1 or int(BMonth) > 12 or len(BMonth) != 2\
    or len(BDay) != 2 or int(BDay) < 1 or int(BDay) > 31:
            print("#######Invalid format of date#######")###checking format 
        else:
            NewUser.update({"Name":Name})
            NewUser.update({"Surname":LName})
            NewUser.update({"Bday":BDate})
            break
##### Greeting user and identification #####
def LogRights():
    global Name, LName, BDay, BMonth, BYear, PDate

    Age = int(PDate.year) - int(BYear)

    if int(BMonth) > PDate.month or (int(BMonth) == PDate.month and int(BDay) < PDate.day):
        Age -= 1 ###counting age based on birth date

    # if (Name.lower() == "jakub") and \
    # (LName.lower() == "marciszonek") and (BDate == "30/01/2004"): 
    #     print(f"------Welcome {Name}, you have {UserRights[0]} rights------")
    #     CurrentRights = UserRights[0]
    #     return CurrentRights
    # elif (Name.lower() == "mira") and (LName.lower() == "vorne") \
    # and (BDate == "11/11/1111"):
    #     print(f"======Welcome {Name}, you have {UserRights[1]} rights======")
    #     CurrentRights = {UserRights[1]}
    #     return CurrentRights
    elif Age >= 18:
        NewUser.update({"Age":Age})
        NewUser.update({"Rights":"Viewer"})
        print(f"Welcome {Name}, you have viewer rights.")
        return 
    else:
        print(f"Greetings {Name}, you are too young to operate this program. Continue")
        return 
    
#### Creates Username#####
def LogReg():
    global BDay, BMonth, BYear, Name, LName, Username
    while True:
        Choice = input("Do you have account?(y/n)")
        QuitCheck(Choice)
        if Choice.lower() == "y"or Choice.lower() == "yes":
            Username = input("Insert your username: ")
            QuitCheck(Username)
            Password = input("Insert your password: ")
            QuitCheck(Password)
            ID = LoginIn(Username, Password)
            if ID != -1:
                print(f"\nWelcome {Username}\n")
                return ID
                
        elif Choice.lower() == "no" or Choice.lower() == "n":
            UserData()
            Choice = input("Would you like to create your username\
or generate it?(Create/Generate)")
            QuitCheck(Choice)
            if Choice.lower() == "generate" or Choice.lower() == "g":
                Username = Name[:2] + LName[:3] + str(BYear) + BMonth + BDay
                while UsernameCheck(Username) == True:
                    Username = Username + str(random.randint(1,9))
                    if UsernameCheck(Username) != True:
                        break
                Choice = input(f"I suggest {Username}(Submit/restart) ")
                QuitCheck(Choice)
                if Choice.lower() == "submit" or Choice.lower() == "s":
                    NewUser.update({"Login":Username})
                    return -1
                else:
                    print("Restarting...")
                    continue
            elif Choice.lower() == "create" or Choice.lower() == "c":
                while True:
                    Username = input("Insert username: ")
                    QuitCheck(Username)
                    if UsernameCheck(Username) != True:
                        NewUser.update({"Login":Username})
                        return -1
                    
            print(f"Your username is:\n{Username}")
        else:
            print("Invalid data")
   
##### Password generator ######
### Characteer selection menu
def CharSelMenu():
    print("Choose characters that are going to be used in password:\n\
1. Digits\n2. Lowercase letters\n3. Uppercase letters\n\
4. Special characters\n5. Generate")
    
### Random character
def RandomChar(Type , Thing):
    Amount = int(input("quantity "))
    QuitCheck(Amount)
    CharacterList = []
    for i in range(Amount):
        CharacterList.append(random.choice(Type))
    print(f"You choosed {Amount} of {Thing}")
    return CharacterList

### Password characters
def PassChar():
    CharacterList = []
    Mistakes = 0
    CharSelMenu()

    while True:
        CharacterChoice = int(input("Choose an option "))
        QuitCheck(CharacterChoice)
        if (CharacterChoice == 5):
            break
        elif (CharacterChoice == 1):
            CharacterList.extend(RandomChar(string.digits, "digits" ))
        elif (CharacterChoice == 2):
            CharacterList.extend(RandomChar(string.ascii_lowercase, "lower letters" ))
        elif (CharacterChoice == 3):
            CharacterList.extend(RandomChar(string.ascii_uppercase, "upper letters" ))
        elif (CharacterChoice == 4):
            CharacterList.extend(RandomChar(string.punctuation, "special characters" ))
        else:
            print("Invalid data")
            Mistakes =+ 1
            if Mistakes >= 5:
                print("Too many invalid data restarting password generation process")
                CharacterList = []
    return CharacterList                    
            
### Password generator
def PasswordCreation():
    while True:
        Choice1 = input("Would you'd like to generate or create your own password:\n\
Password have to be min 5 characters long(Generate/Create)")
        QuitCheck(Choice1)
        if Choice1.lower() == "generate" or Choice1.lower() == "gen" or Choice1.lower() == "g":
            while True:
                Password = []
                Password.extend(PassChar())#####extend rozpakowuje przed dodaniem do listy
                if len(Password) >= 5:
                    random.shuffle(Password)
                    print(f"The random password is \"{"".join(map(str, Password))}\"")
                    PasswordSub = str(input("Do you want to submit, generate or restart the password?\n\
(Submit/Restart/Generate): "))
                    if PasswordSub.lower() == "submit" or "sub" or "s":
                        NewUser.append({"Password":"".join(Password)})
                        return 
                    elif PasswordSub.lower() == "restart" or "res" or "r":
                        break
                    else:
                        print("Invalid data\nRestarting the generator")
                        continue
                else:
                    print("Reminder password have to have min 5 characters.")
                    continue 
        elif Choice1.lower() == "create" or Choice1== "c":
            while True:
                Password = input("Create your password(min no of characters is 5): \n")
                if len(Password) >= 5:
                    Choice = input(f"Do you want to submit that password(Submit/again/restart):\n{Password}")
                    QuitCheck(Choice)
                    if Choice.lower() == "submit" or "sub" or "s":
                        NewUser.update({"Password":Password})
                        print("Submited")
                        return
                    elif Choice.lower() == "again" or "a":
                        continue
                    else:
                        break
        else:
            continue
##### Movement detection #####
### test version with random input
def MoveDet():
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
def TempConEva():
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




##### working main
def main():
    print("Hello user, welcome to the Motion Detector! Let's start.\n\
type quit whenever you would like to end the session.")
    while True:
        ID = LogReg()
        if ID < 0:###The ID is position of user in list so it cannot
            LogRights()###have negative value
            PasswordCreation()
        # MoveDet()
        # TempConEva()
        break

def NoGame():
    Wins = 0
    Loses = 0
    
    print("Welcome at number guessing game\nYou can guess numbers from 1 to 100")
    
    while True:
        Turns = 0
        No = random.randint(1,100)
        while Turns < 8:
            UNo = input("Guess the number: ")
            QuitCheck(UNo)
            if str(UNo).lower() == "exit":
                print("Exiting the game")
                return
            elif int(UNo) == No:
                Wins += 1
                print("You guessed correctly!!!")
                break
            elif int(UNo) > No:
                Turns += 1
                print("Your guess is too high")
            elif int(UNo) < No:
                Turns += 1 
                print("Your guess is too low")
            else:
                print("Command didn't recognized")
        if Turns > 8:
            Loses += 1
        print(f"You won {Wins} times\nYou lost {Loses} times\nIn {Turns} turns.")
        print("If you would like to exit just type exit if not let me continue")


#### working main
# main()
# print(NewUser)
# with open("data/Users.json", "r") as file:
#     Data = json.load(file)

# Data["Users"].append(NewUser)

# with open("data/Users.json", "w") as file:
#     json.dump(Data, file)
# print("You are registered")
# with open("data/Users.json", "r") as file:
#     print(json.load(file))