import requests
import json
import os
import replit
from pprint import pprint

API_KEY = os.environ.get("API_KEY")


def jsonify(call):
  r = requests.get(call)
  print(r.json())

pwd = input("What's the password for this program? ")
if (pwd != os.environ.get("PASSWORD")):
  exit()


def convert_to_uuid():
  return jsonify(f"https://api.mojang.com/users/profiles/minecraft/{player_name}").get("id")

endpoint = "https://api.hypixel.net/v2/"


player_name = input("Player Name: ")
player_uuid = convert_to_uuid()

replit.clear()
choices = input('''What stats would you like to see?
1 - Skyblock
2 - Bedwars
3 - Skywars
4 - Duels
5- General Player Stats''')

loop = True

while loop:
  if (choices == "1"):
    new_endpoint = f"{endpoint}/skyblock/profiles?key={API_KEY}&uuid={player_uuid}"
  elif (choices == "2"):
    new_endpoint = f"{endpoint}/bedwars?key={API_KEY}&uuid={player_uuid}"
  elif (choices == "3"):
    new_endpoint = f"{endpoint}/skywars/profiles?key={API_KEY}&uuid={player_uuid}"
  elif (choices == "4"):
    new_endpoint = f"{endpoint}/duels/profiles?key={API_KEY}&uuid={player_uuid}"
  elif (choices == "5"):
    new_endpoint = f"{endpoint}/player?key={API_KEY}&uuid={player_uuid}"
  else:
    print("Hey man, that's not one of the choices that were avaliable.")
    replit.clear()
  


if (player_uuid == "None"):
  print("Username not found.")
  exit()
elif (jsonify(skyblock_link).get("profiles") == None):
  print("No profile found.")
  exit()
elif (jsonify(skyblock_link)):
  print("Could not connect to the hypixel API.")
else:
  print(player_uuid)
  pprint(jsonify(skyblock_link))
  print(skyblock_link)
