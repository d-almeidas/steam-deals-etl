import requests

params = {"id": "1091500"}
url = "https://store.steampowered.com/api/featuredcategories/?cc=br&l=portuguese"
req = requests.get(url, params=params)

print(req.status_code)
print(req.json())