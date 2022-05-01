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

#parse the url to xml string
url = input('Enter location: ')
xml = urllib.request.urlopen(url, context=ctx).read() 

tree = ET.fromstring(xml)  
#count_list = tree.findall('comments/comment')  
#count tags在comments/comment tags下面

# or 如果生孩子层数过多，直接找到comment：
count_list = tree.findall('.//comment')
print('Count:', len(count_list))
print(count_list)

sum = 0
for tag in count_list:
    sum = sum + int(tag.find('count').text)
    
print('Sum: ' ,sum)


