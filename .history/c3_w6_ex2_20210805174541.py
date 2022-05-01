import json
import ssl
import urllib.error
import urllib.parse
import urllib.request

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True: #一次loop 代表用户输入一个地址，返还给她这个地址的lat,lng,loc这些信息 一次
    #用户输入input
    address = input('Enter location: ') #user input loc, like: Ann Arbor, MI
    if len(address) < 1: break #while循环有break条件可以触发

    #确定成具体的url
    url = serviceurl + urllib.parse.urlencode({'key':key,'address':address})  
    #将输入的location转化成url，concate with service网址
    print('Retrieving', url) #我们正在retrieval什么url
    
    #urllib开始parse解析url为string 
    uh = urllib.request.urlopen(url,context=ctx) #parse the url as a object
    data = uh.read().decode() #object to a string；decode to unicode
    print('Retrieved', len(data), 'characters') #查看length
    
    #用json读string成dict
    try:
        js = json.loads(data) #用json读data 成python dict
    except:
        js = None #防止traceback
    if not js or 'status' not in js or js['status'] != 'OK': 
        #如果js或里面的status tag不对，就continue
        print('===failure to retrieve===')
        print(data)
        continue
    
    #如果想在terminal打印出此时的dict整齐的样子，便于后面找信息
    print(json.dumps(js, indent=4)) #indent=4比较好看
    
    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
    
