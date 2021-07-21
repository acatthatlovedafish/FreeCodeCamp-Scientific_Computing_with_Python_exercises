import urllib.request, urllib.parse, urllib.error
import json

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')

    parms = dict()
    parms['address'] = address
    if api_key is not False: 
        parms['key'] = api_key

    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    js = json.loads(data)

    place_id = js['results'][0]['place_id']
    print("Place id", place_id)