import urllib.request, urllib.parse, urllib.error  #用于解析
import json 

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'  #service网址

while True:
    #用户输入input
    address = input('Enter location: ') #user input loc, like: Ann Arbor, MI
    if len(address) < 1: break #while循环有break条件可以触发

    #确定成具体的url
    url = serviceurl + urllib.parse.urlencode({'address':address})  
    #将输入的location转化成url，concate with service网址
    print('Retrieving', url) #我们正在retrieval什么url
    
    #开始parse解析url为string 
    uh = urllib.request.urlopen(url) #parse the url as a object
    data = uh.read().decode() #object to a string；decode to unicode
    print('Retrieved', len(data), 'characters') #查看length
    
    #用json读data
    try:
        js = json.loads(data) #用json读data
    except:
        js = None #防止traceback
    if not js or 'status' not in js or js['status'] != 'OK': 
        #如果js或里面的status tag不对，就continue
        print('===failure to retrieve===')
        print(data)
        continue
    
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)