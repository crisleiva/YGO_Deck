import urllib3
import urllib.request
import time
import json
import os
#This file handles our api. We make requests to the url below and return it as json.
YGO_URL = "https://db.ygoprodeck.com/api/v5/cardinfo.php"
http = urllib3.PoolManager()

def api_call():
	time.sleep(6)
	ygo_cards = http.request('GET', YGO_URL)
	ygo_json = json.loads(ygo_cards.data.decode('UTF-8'))
	return ygo_json

#The code below takes in the json and returns only the image links provided with each card.	
def find_img_link(data):
	print("Images are being returned")
	array = []
	for dic in data:
		for key in dic:
			if key == "card_images":
				for image in dic[key]:
					for url in image:
						if url == "image_url" or url == "image_url_small":
							array.append(image[url])
	return array
#The code store_image will take in each url and download it into a folder to store each picture locally.
def store_image(url):
	print("Download starting...")
	file_path = "/Users/cristianleiva/Development/YGODeck/backend/ygo/images"
	for text in url:
		size = text.split('/')[4]
		f_name = text.split('/')[-1]
		full_path = file_path + '/' + size + '/' + f_name
		print(f"Starting new download for image {f_name}....")
		urllib.request.urlretrieve(text, full_path)

store_image(find_img_link(api_call()))