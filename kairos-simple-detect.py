import requests
import json
# put your keys in the header
headers = {
    "app_id": "b974ce92",
    "app_key": "d5c6c9067bf7c769d66598d9452db856"
}

payload = '{"image":"https://lh3.googleusercontent.com/382qqKI4fG9J2AnMziQsk-8313XMXUYVgxBYqrVRW8YmoiWChn-y8aN8hf9jwQs6B0rS21MFx9bIaCll5-ROIBX6-ERr4mTWgIFnMwTZ2xd6YvliNl-IryDDeb6Z6oEKH0d6Do5wo63TWjMH9zqHwF_brMNME0-OWQS9A7jBCI91RsQs7WT3_3Qof1FqxDrM2Zjv58AzK4RHG7CA0hOBPolaWr2HbI_5PWHhFas_VQRuChb8QsGed84HRO37AmyEJc_1t6_vsKzJFFBecLaMRpgSQ8wtS2KarluvrBnXvbc-M3BLO_WVzF1fngCXZ1i8lalF5Z3I-IQ9Ap5m0l9Wbvm2xpVfN6qmmlqlTiNjJCTKu8YLkvi5nr3y2U45NSdjYOGGWovJlACyk4I_wL379ALqfDd5J7QlYUkGNBbuynChaCfAENjr_KSIFsGpFftRhluR3lmOzsU2NsDttNHahlfmV_xM1yve4M-ZqpVgQv5NDRGoE6q1rWzNGS01NUm__csCAgPzB-wE02KVJOxSfmP3KWZEY8JpXfMItu9TFZ4WThXdSVHBJP-LRlbG4bT4HiqfV37qRT1h0TAumpuLmXh6xBuyS6BcUjrr8Ng=w447-h595-no"}'

url = "http://api.kairos.com/detect"

# make request
r = requests.post(url, data=payload, headers=headers)
parsed =json.loads(r.content.decode('utf-8'))
print (json.dumps(parsed, indent=4, sort_keys=True))
