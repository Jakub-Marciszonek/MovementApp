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

###Data in Use###

NewUser = {}
data = ""

##### Data update #####

def AddUser(Path, NewUser):
    with open(Path, "r") as file:
        Data = json.load(file)
    print(f"Download\n{Data}")
    Data["Users"].append(NewUser)
    print(Data)
    with open(Path, "w") as file:
        json.dump(Data, file, indent=4)
    return  len(data["Users"]) - 1

def UpdateAPI(API):
    global data
### https://api.thingspeak.com/channels/2578404/feeds.json?api_key=XSXF6WH7DAECB6S1&results=20
    response = requests.get(API)
    if response.status_code != 200:
        print("API data couldn't be updated")
        return
    data = response.json()###download

    with open("data/TempNMove.json", "w") as file:
        json.dump(data, file, indent=4)

##### Quit function #####

def QuitCheck(inp):
    if str(inp).lower() == "quit":
        sys.exit()

##### Replace character in str #####

def ReplaceChar(Str, Char, NewChar):
    if Str.count(Char) > 0:
        for i in range(Str.count(Char)):
            No = Str.find(Char)
            Str = list(BDate)
            Str[No] = NewChar
            Str = "".join(Str)

##### Checkes if somebodies username is already saved #####
def LogCheck(Username, Password):                            
    with open("data/Users.json", "r") as file:
        data = json.load(file)
    for i in range(len(data["Users"])):
        if Username == data["Users"][i]["Login"]:
            ID = i
        else:
            ID = -1
        if Password == data["Users"][i]["Password"]:
            PassNr = i
        else:
            PassNr = ID - 1
        if ID == PassNr:
            print("Succsesfully loged in")
            return ID
    print("Incorrect Login or Password")
    return -1

def UsernameCheck(Username):
    with open("data/Users.json", "r") as file:
        data = json.load(file)
    for i in data["Users"]:
        print(i)
        if Username == i["Login"]:
            print("Username is occupied")
            return True
        else:
            return {"Login":Username}
###### Personale data input ######
def UserData():
    
    global Name, LName, BDate, BDay, BMonth, BYear
    while True:
        Name = str(input("What's ur name? ")).title()###name and birthday
        QuitCheck(Name)
        if str(Name).lower() == "back":
            return
        if Name != "":
            break
    while True:
        LName = str(input("What's ur lastname? ")).title()
        QuitCheck(LName)
        if str(LName).lower() == "back":
            return
        if Name != "":
            break

    while True:
        while True:
            BDate = input("When you've been born write? \
    The date in (dd/mm/yyyy) format. \n")
            QuitCheck(BDate)
            if str(BDate).lower() == "back":
                return
            
            ReplaceChar(BDate, "-", "/")
            ReplaceChar(BDate, ".", "/")
            ReplaceChar(BDate, " ", "/")

            if len(BDate) == 10 and BDate.count("/") == 2:
                break
            print("#######Invalid format of date#######")

        

        BDay, BMonth, BYear = map(str, BDate.split("/"))# map is deviding one 
        # variable into 3 new ones respectivly by .split function where separator
        # is defined as /

        if (len(BYear) != 4) or int(BMonth) < 1 or int(BMonth) > 12 or len(BMonth) != 2\
or len(BDay) != 2 or int(BDay) < 1 or int(BDay) > 31 or PDate.strftime("%Y")\
 < BYear or PDate.strftime("%Y") == BYear and PDate.strftime("%m") < BMonth:
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

    elif Age >= 18:
        NewUser.update({"Age":Age})
        NewUser.update({"Rights":"Viewer"})
        print(f"Welcome {Name}, you have viewer rights.")
        return 
    else:
        print(f"Greetings {Name}, you are too young to operate this program. Continue")
        return 
    
#####Log in #####
def Login():
    while True:
        Username = input("Insert your login: ")
        QuitCheck(Username)
        if str(Username).lower() == "back":
            break
        Password = input("Insert your password: ")
        QuitCheck(Password)
        if str(Password).lower() == "back":
            break
        ID = LogCheck(Username, Password)
        if ID != -1:
            print(f"\nWelcome {Username}\n")
            return ID
        else:
            print("Invlid data")
##^^^Login^^^##
def Registration():
    global BDay, BMonth, BYear, Name, LName, Username
#### Creates Username#####
    while True:
        UserData()
        Choice = input("Would you like to create your username\
or generate it?(Create/Generate)")
        QuitCheck(Choice)
        if str(Choice).lower() == "back":
            return
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
                if str(Username).lower() == "back":
                    return
                if UsernameCheck(Username) != True:
                    NewUser.update({"Login":Username})
                    continue
                else:
                    print("Invalid data")
                
        print(f"Your username is:\n{Username}")
##^^^ Registration part ^^^##
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
                        NewUser.update({"Password":"".join(Password)})
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
    print("~~~Movement Detectort & Celsius to Fahrenheit calculator~~~")
    # Movement = data["feeds"][len(data["feeds"]) - 1]["Movement"]
    ###last entry
    for i in data["feeds"]:
        if (i["field1"] == "1"):
            print("Movement detected")
            print(f"Created in {i["created_at"][:10]}")
            print(f"at {i["created_at"][11:16]}\n")
        elif (i["field1"] == "0"):
            print("Movement not detected")
            print(f"Created in {i["created_at"][:10]}")
            print(f"at {i["created_at"][11:16]}\n")
        else:
            print("\nInvalid data")
    input("")

##### Temperature converter and evaluator #####
def Temp():
        TemD = (input("Choose the units that you want to display\
\n1. Celsius degrees\n2. Fahrenheit degrees\n"))
        for i in data["feeds"]:
            if TemD == "1":###Celsius to Fahrenheit converter
                print(f"The temperature is {i["field2"]}C°")
                print(f"Created in {i["created_at"][:10]}")
                print(f"at {i["created_at"][11:16]}\n")
            elif TemD == "2":
                FDegrees = (float(i["field2"])*9/5) + 32
                print(f"The given temperature {i["field2"]}C° is equal to {FDegrees:.2f}F°")
                print(f"Created in {i["created_at"][:10]}")
                print(f"at {i["created_at"][11:16]}\n")
            else:
                print("Invalid data")

            if float(i["field2"]) <= 40:
                print("CPU is dead cold")
            elif float(i["field2"]) > 80:
                print("[*]RIP CPU [*]")
            elif float(i["field2"]) > 65:
                print("It's getting hot here ( ͡° ͜ʖ ͡°)")
            else:
                print("ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧")
        input("")

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
###menu
    
def Menu1():
    ID = -1
    print("Hello user, welcome to the Motion Detector! Let's start.\
type quit whenever you would like to end the session.\n")
    while True:
        UpdateAPI("https://api.thingspeak.com/channels/2578404/feeds.json?api_key=XSXF6WH7DAECB6S1&results=5&timezone=Europe/Helsinki")
        if ID >= 0:
            Menu2()
            return
        print("~~~~~Login Menu~~~~~")
        print("1.Login\n2.Register\n0.Exit")
        MenuChoice = input("")
        if MenuChoice.isnumeric():
            MenuChoice = int(MenuChoice)
        else:
            print("Invalid input")
        
        if MenuChoice == 1:
            print("When you want to go back into menu write \"back\"")
            ID = Login()
        elif MenuChoice == 2:
            print("When you want to go back into menu write \"back\"")
            Registration()
            LogRights()
            PasswordCreation()
            ID = AddUser("data/Users.json", NewUser)
            
        MenuExit(MenuChoice)

def Menu2():
    while True:
        MenuChoice = int(input("1 - Movement detection\
    \n2 - Temperature\n0 - Log out\n"))
        if MenuChoice == 1:
            MoveDet()
        if MenuChoice == 2:
            Temp()
        if MenuChoice == 0:
            return

def MenuExit(MenuChoice):
    QuitCheck(MenuChoice)
    if MenuChoice == 0:
        print("Shutting down the program")
        sys.exit()

def main():
    Menu1()

main()