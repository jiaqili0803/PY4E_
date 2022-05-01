'''look through all the <comment> tags 
find the <count> values sum the numbers
use an XPath selector string to look through the entire tree of XML for any tag named 'count' with the following line of code:

counts = tree.findall('.//count')'''
#####################ex1
import ssl
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

##ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
tree = ET.parse(url)  
count_list = tree.findall('count') 
print('Count:', len(count_list))

sum = 0
for tag in count_list:
    sum = sum + int(tag.find('count').text)
    
print('Sum: ' ,sum)
    