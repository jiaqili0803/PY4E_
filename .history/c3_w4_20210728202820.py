#urllib library
import urllib.request, urllib.parse, urllib.error
file = urllib.request.urlopen('') #'': parse解析 the url 
#file: the urllib library return the web page looks like a file 
for line in file:
    print(line.decode().strip())   
