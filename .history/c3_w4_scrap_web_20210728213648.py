#BeautifulSoup to scrape
import urllib.error
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup

url = input('Enter: ')
html = urllib.request.urlopen(url).read() 
#read(): 把一个object的file 读成一个长string
#print(html)
soup = BeautifulSoup(html, 'html.parser') 
print(soup)
print(type(soup))
#use BeautifulSoup to read and parse and 自动整理爬下来的内容 to a object'soup'
#soup is just a name, can be changable
