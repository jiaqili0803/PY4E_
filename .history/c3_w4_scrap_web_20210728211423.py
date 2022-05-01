#BeautifulSoup to scrape
import urllib.error
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup

url = input('Enter: ')
html = urllib.request.urlopen(url)
print(html)
