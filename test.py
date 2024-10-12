import requests
import json


Feeds = []
url = "https://api.thingspeak.com/channels/2578404/feeds.json?api_key=XSXF6WH7DAECB6S1&results=20"
response = requests.get(url)
print(f"Status code: {response.status_code}")
data = response.json()### downloaded data
for entry in data["feeds"]:
    movement_value = entry["field1"]
    temp_value = entry["field2"]
    time_value = entry["created_at"]
    print(f"Movement value: {movement_value}")
    print(f"Temperature value: {temp_value}")
    print(f"At: {time_value}")
    Feed = {"Movement": movement_value, "Temp": temp_value, "Time": time_value}
    ###One dictionary
    Feeds.append(Feed)
    
Feeds = {"feeds": Feeds}
print(Feeds)
with open("data/TempNMove.json", "w") as file:
    json.dump(Feeds, file)
with open("data/TempNMove.json", "r") as file:
    data1 = json.load(file)
print(data1)