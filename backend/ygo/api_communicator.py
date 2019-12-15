import urllib3
import requests
import json
import os

YGO_URL = "https://db.ygoprodeck.com/api/v5/cardinfo.php"
http = urllib3.PoolManager()
ygo_cards = http.request('GET', YGO_URL)
ygo_json = json.loads(ygo_cards.data.decode('UTF-8'))

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

def store_image(url):
	print("Download starting...")
	for text in url:
		size = text.split('/')[4]
		f_ext = text.split('/')[-1]
		print(size, f_ext)

store_image(find_img_link(ygo_json))

