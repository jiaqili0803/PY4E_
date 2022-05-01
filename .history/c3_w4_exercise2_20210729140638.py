###Find the link at position 18 (the first name is 1). Follow that link. Repeat this process 7 times. The answer is the last name that you retrieve.


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

count = int(input('Enter count: ' ))
position = int(input('Enter position: ' ))

all_name = list()
first_name = list()
for i in range(7):
    if i == 0:
        url = input('Enter URL: ' )
        first_name = re.findall('known_by_(.+).html', url)
    else:
        url = names_list[17]
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of the anchor tags
    #count = 0
    names_list = list() #建list：= list() or =[]
    tags = soup('a')
    for tag in tags:
        #print(tag.get('href', None))
        #count = count + 1
        #print(count)
        names_list.append(tag.get('href', None))
    print('name list:',names_list[2])   #get a name_url list
    name = re.findall('known_by_(.+).html', names_list[17])
    print('name: ', name)
    all_name.append(name[0])

print('all name:', first_name + all_name)


