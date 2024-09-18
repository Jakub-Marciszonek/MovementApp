import random

print("Welcom in rock, paper scissors game.\
\nR=rock\nP=paper\nS=scissors\n")

Dupa = ["R","P","S"]
CChoice = random.choice(Dupa)

PInput = str(input("Choose ur move "))
print(CChoice)

if PInput == CChoice:
    print("tie")

elif (PInput == "R") and  CChoice == "S":
    print("You won!!!")
elif (PInput == "R") and CChoice == "P":
    print("You lose")

elif (PInput == "P") and  CChoice == "P":
    print("You won!!!")
elif (PInput == "P") and CChoice == "S":
    print("You lose")

elif (PInput == "S") and  CChoice == "P":
    print("You won!!!")
elif (PInput == "S") and CChoice == "R":
    print("You lose")

else:
    print("invalid data")