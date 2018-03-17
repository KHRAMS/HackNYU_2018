
import requests

# put your keys in the header
headers = {
    "app_id": "b974ce92",
    "app_key": "d5c6c9067bf7c769d66598d9452db856"
}

payload = '{"image":"/home/katchu11/Pictures/liz.jpg"}'

url = "http://api.kairos.com/detect"

# make request
r = requests.post(url, data=payload, headers=headers)
print (r.content)
