import urllib.request, json
with urllib.request.urlopen("https://api.skypicker.com/flights?flyFrom=PRG&to=LGW&dateFrom=18/02/2019&dateTo=19/02/2019&partner=picky") as url:
    data = json.loads(url.read().decode())
    print(data)