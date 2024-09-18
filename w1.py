##### Chapter W1 #####
import datetime

print("Hello user, welcome to the Motion Detector! Let's start.")### user input:
Name = str(input("What's ur name? "))###name and birthday
LName = str(input("What;s ur lastname? "))
BDate = input("When you've been born write? \
The date in (dd/mm/yyyy) format. \n")
BDay, BMonth, BYear = map(str, BDate.split("/"))# map is deviding one 
# variable into 3 new ones respectivly by .split function where separator
# is defined as / 
PDate = datetime.datetime.now()

Age = int(PDate.year) - int(BYear)
if (int(BMonth) > int(PDate.month) and int(BDay) > int(PDate.day)):
    Age = Age-1 ###counting age based on birth date

if (len(BYear) != 4) or (int(BMonth) < 1 or int(BMonth or len(BMonth) != 2 ) > 12)\
or ((len(BDay) != 2) or (int(BDay) < 1) or (int(BDay) > 31)):
    print("Invalid format of date")

print(f"Hello {Name} {LName}, welcome to the Motion Detector! \
Let’s start. Your username is: ")

print(Name[:2] + LName[:3] + BYear + BMonth + BDay)


Movement = input("There was a movement in the room? (y/n) \n")
if (Movement == "YES") or (Movement == "yes") or (Movement == "y"):
    print("Movement detected")
elif (Movement == "NO") or (Movement == "no") or (Movement == "n"):
    print("Movement not detected")
else:
    print("Invalid data")### movement detection



print("Celsius to Fahrenheit calculator")###Celsius to Fahrenheit converter
CDegrees = float(input("Enter the Celsius Degrees: "))
FDegrees = round((CDegrees *1.8 + 32), 2)

# TemD = int(input("Choose the units\
# \n1. Celsius degrees\n2. Fahrenheit degrees\n"))
# if TemD == "1":
#     print()
# elif TemD == "2":
#     print()
# else:
#     print("Invalid data")

# print(f"The given temperature {CDegrees}C° is {FDegrees}F°")
##### Chapter W2 #####