import urllib.request
import json

address = input("Enter location: ")
print('Retrieving', address)

url = urllib.request.urlopen(address).read().decode()
print('Retrieved', len(url), 'characters')
js = json.loads(url)
info = js["comments"]

summa = 0
count = 0
for item in info:
    count += 1
    summa += item["count"]
print("Count:", count)
print("Sum:", summa)