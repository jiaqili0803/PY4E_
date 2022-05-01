###ex2 提取网页上的link的link的link的自动化套娃行为
# Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.


import re
import ssl
import urllib.error
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#让用户enter的舒适行为
count = int(input('Enter count: ' ))
position = int(input('Enter position: ' ))

all_name = list()
first_name = list()
for i in range(count):
    if i == 0:  #第一次人工copylink，后面自动
        url = input('Enter URL: ' )
        first_name = re.findall('known_by_(.+).html', url)
    else:
        url = names_list[position-1]
    html = urllib.request.urlopen(url, context=ctx).read() #读取解析url
    soup = BeautifulSoup(html, 'html.parser')

    ## Retrieve all of the anchor tags
    names_list = list() #建list：= list() or =[]；=()出来是tuple！！
    tags = soup('a')
    for tag in tags:
        #print(tag.get('href', None))
        names_list.append(tag.get('href', None))  #提取’herf‘后面对应的东西
    print('Retrieving:',names_list[position-1])   #get a name_url list
    name = re.findall('known_by_(.+).html', names_list[position-1]) 
    #re来提取每个里面的名字
    print('name: ', name)
    all_name.append(name[0]) 

print('all name:', first_name + all_name) #加上初始name和所有提取出的name的list集合


