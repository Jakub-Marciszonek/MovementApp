##### Chapter W1 #####
print("Hello user, welcome to the Motion Detector! Let's start.")
Name = str(input("What's ur name? "))
LName = str(input("What;s ur lastname? "))
BDate = input("When you've been born write? \
The date in (dd/mm/yyyy) format. ")
BDay, BMounth, BYear = list(str, BDate.split("/"))# map is deviding one 
# variable into 3 new ones respectivly by .split function where separator
# is defined as / 

print(f"Hello {Name} {LName}, welcome to the Motion Detector! \
Let’s start. Your username is: ")

print(Name[:2] + LName[:3] + BYear + BMounth + BDay)


Movement = input("There was a movement in the room? (y/n) ")
if (Movement == "YES") or (Movement == "yes") or (Movement == "y"):
    print("Movement detected")
elif (Movement == "NO") or (Movement == "no") or (Movement == "n"):
    print("Movement not detected")
else:
    print("Invalid data")



print("Celsius to Fahrenheit calculator")
CDegrees = float(input("Enter the Celsius Degrees: "))
FDegrees = round((CDegrees *1.8 + 32), 2)


print(f"The given temperature {CDegrees}C° is {FDegrees}F")
##### Chapter W2 #####