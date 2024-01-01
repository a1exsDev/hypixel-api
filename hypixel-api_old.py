import requests
import json
import os
from pprint import pprint


def getInfo(call):
  r = requests.get(call)
  return r.json()


def convert_to_uuid():
  return getInfo(f"https://api.mojang.com/users/profiles/minecraft/{player_name}").get("id")


API_KEY = os.environ.get("API_KEY")

player_name = input("Player Name: ")
player_uuid = convert_to_uuid()

skyblock_link = f"https://api.hypixel.net/v2/skyblock/profiles?key={API_KEY}&uuid={player_uuid}"

if (player_uuid == "None"):
  print("Username not found.")
  exit()
elif (getInfo(skyblock_link).get("profiles") == None):
  print("No profile found.")
  exit()
elif (getInfo(skyblock_link).get("success") == False):
  print("Could not connect to the hypixel API.")
else:
  print(player_uuid)
  pprint(getInfo(skyblock_link))
  print(skyblock_link)
