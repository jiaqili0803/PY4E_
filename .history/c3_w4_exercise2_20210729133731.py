import ssl
import urllib.error
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
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
print('name list:',names_list)   #get a name_url list
#print('length of name list: ', len(names_list))

# 4times loop
url_name = input(names_list[2])
