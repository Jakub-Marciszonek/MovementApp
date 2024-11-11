import json

with open("MovementApp\data\Users.json", "r") as file:
    data = json.load(file)
print(len(data["Users"]))