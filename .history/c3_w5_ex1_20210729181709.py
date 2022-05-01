look through all the <comment> tags 
find the <count> values sum the numbers
use an XPath selector string to look through the entire tree of XML for any tag named 'count' with the following line of code:

counts = tree.findall('.//count')
#####################ex1
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = input('Enter location: ')
stuff = ET.fromstring(url)  
lst = stuff.findall('users/user') 