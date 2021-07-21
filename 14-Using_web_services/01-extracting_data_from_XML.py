import urllib.request
import xml.etree.ElementTree as ET

address = input("Enter location: ")
print('Retrieving', address)

url = urllib.request.urlopen(address).read()
print('Retrieved', len(url), 'characters')

tree = ET.fromstring(url)
counts = tree.find("comments").findall("comment")
print("Count:", len(counts))

total_count = 0
for item in counts:
    count = item.find("count").text
    count = int(count)
    total_count += count
print("Sum:", total_count)
