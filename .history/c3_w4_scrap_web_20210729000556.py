########BeautifulSoup to scrape
import ssl
import urllib.error
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup

##ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter: ')
html = urllib.request.urlopen(url, context=ctx).read() 

#read(): 把一个object的file 读成一个长string
#print(html)
soup = BeautifulSoup(html, 'html.parser') 
print(soup)
#use BeautifulSoup to read and parse and 自动整理爬下来的内容 to a object'soup'
#soup is just a name, can be changable

########retrieve all the anchor tags (with'a' about 'herf'
tags_with_a = soup('a')  #ask for the anchor tags with 'a'
for tag in tags_with_a:
    print(tag.get('herf', None)) 
    #dict的get(): 字典的方法，得到herf们对应的links，或者none
