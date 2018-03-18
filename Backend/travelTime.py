import urllib.request, json

endpoint = "https://maps.googleapis.com/maps/api/distancematrix/json?"
api_key = "AIzaSyBTr-wJwTkr6VUt3xboaCyZBtQk_ST_GHY"
origin = input("Where are you?:").replace(" ", "+")
destination = input("Where do you want to go?:").replace(" ", "+")
departure = input("What time are you starting?:")
arrivaltime = input("What time do you want to be there by?:")
nav_request = 'origins={}&destinations={}&departure_time={}&arrival_time{}&key={}'.format(origin,destination,departure,arrivaltime,api_key)
request = endpoint + nav_request
response = urllib.request.urlopen(request).read()
data = json.loads(response)
print(data)
#18205 Warbler Way, West Windsor, NJ 08550
#6 MetroTech Center, Brooklyn, NY 11201


