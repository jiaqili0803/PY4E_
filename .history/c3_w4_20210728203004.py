#urllib library
import urllib.request, urllib.parse, urllib.error
file = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') #'': parse解析 the url 
#file: the urllib library return the web page looks like a file 
for line in file:  #read each line
    print(line.decode().strip())   #decode(): bytes to strings
