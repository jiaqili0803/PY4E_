#urllib library
import urllib.request, urllib.parse, urllib.error
file = urllib.request.urlopen('') #'': parse解析 the url 
#file: the urllib library make the web page look like a file for us
for line in fine:
    print(line.decode().strip())   
