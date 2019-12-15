import urllib3
import json


YGO_URL = "https://db.ygoprodeck.com/api/v5/cardinfo.php"
http = urllib3.PoolManager()
ygo_cards = http.request('GET', YGO_URL)
ygo_json = json.loads(ygo_cards.data.decode('UTF-8'))

def find_img_link(data):
	for dic in data:
		for key in dic:
			if key == "card_images":
				for image in dic[key]:
					for url in image:
						if url == "image_url" or url == "image_url_small":
							print("Images are being returned")
							return image[url]

def store_image(image)

find_img_link(ygo_json)