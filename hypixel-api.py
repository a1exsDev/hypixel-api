import requests
import json
from pprint import pp, pprint

def getInfo(call):
    r = requests.get(call)
    return r.json()

def convert_to_uuid():
    return getInfo(f"https://api.mojang.com/users/profiles/minecraft/{player_name}").get("id")

API_KEY = "c0b5fc9f-7432-4807-a996-cb1a2e3785a9"

player_name = input("Player Name: ")
player_uuid = convert_to_uuid()

uuid_convert = f"https://api.mojang.com/users/profiles/minecraft/{player_name}"
skyblock_link = f"https://api.hypixel.net/v2/skyblock/profile?key={API_KEY}&uuid={player_uuid}"


pprint(getInfo(skyblock_link))
print(skyblock_link)