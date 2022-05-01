########BeautifulSoup to scrape web 抓取网页上我们想要的东西
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
soup = BeautifulSoup(html, 'html.parser') 
#use BeautifulSoup to read and parse and 自动整理爬下来的内容 to a object'soup'
#soup is just a name, can be changable

########retrieve all the anchor tags 
# (这里是with'a' about 'href'，想要抓什么可以浏览器url前面加：view-source:看
tags_with_a = soup('a')  #ask for the anchor tags with 'a'
for tag in tags_with_a:
    print(tag.get('href', None)) 
    #dict的get(): 字典的方法，得到href们对应的links，或者返回none；这里相当于抓取了每个href后面跟着的网址
