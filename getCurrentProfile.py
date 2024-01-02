import requests, json, os, random
from pprint import pprint

API_KEY = os.environ.get("API_KEY")
endpoint = "https://api.hypixel.net/v2/skyblock/profiles"

def jsonify(call):
	r = requests.get(call)
	return r.json()

def convert_to_uuid():
	return jsonify(f"https://api.mojang.com/users/profiles/minecraft/{player_name}").get("id")

player_name = random.choice(["Technoblade", "TimeDeo", "Shiiyu", "Cookie_Wookie_7"])
player_uuid = convert_to_uuid()

new_endpoint = f"{endpoint}?key={API_KEY}&uuid={player_uuid}"
def getCurrentProfile():
	for x in jsonify(new_endpoint)["profiles"]:
		if (x["selected"] == True):
			return x["cute_name"]


#pprint(jsonify(new_endpoint))
#print(new_endpoint)
print(player_name)
print(player_uuid)
if (jsonify(new_endpoint).get("success") == False):
	print(f"Could not connect to the Hypixel API due to {jsonify(new_endpoint).get('cause')}")
	exit()
#print(jsonify(new_endpoint))
print(getCurrentProfile())

#print(player_name)
