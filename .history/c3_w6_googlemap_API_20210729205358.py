import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True:
    address = input('Enter location: ')  #user input the location they want to know, like: Ann Arbor, MI
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address':address}) 
    #将输入的location转化成url，concate with 'https://maps.googleapis.com/maps/api/geocode/xml?'这个固定的url前半部分
    print('Retrieving', url) #我们正在retrieval什么url
    uh = urllib.request.urlopen(url) #parse the url as a object

    data = uh.read().decode() #object read to a string
    print('Retrieved', len(data), 'characters') #length
    #decode as unicode we can use in python
    
    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'status' not in js or js['status'] != 'OK':
        print('===failure to retrieve===')
        print(data)
        continue
    
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js
    print(location)