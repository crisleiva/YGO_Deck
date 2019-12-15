import requests
from flask import jsonify
YGO_URL = "https://db.ygoprodeck.com/api/v5/cardinfo.php"

def api_call():
	res = requests.get(YGO_URL)
	return jsonify(res.json())

# def store_image(data):
# 	for info in data[0]["card_images"]:
# 		for value in info:
# 			print(info[value])

# store_image(api_call)