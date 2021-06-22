import requests

API_KEY = "cfb834573a490312f5eb78d5411fa7b5"
WS_URL = "http://api.weatherstack.com/current"

cities = []
with open("cities.txt") as f:
    for line in f:
        cities.append(line.strip())
print(cities)

for city in cities:
    parameters = {'access_key': API_KEY, 'query': city}
    response = requests.get(WS_URL, parameters)
    js = response.json()

    temperature = js['current']['temperature']
    date = js['location']['localtime']
  

    with open(f"{city}.txt", "a") as f:
        f.write(f"{date},{temperature}\n")