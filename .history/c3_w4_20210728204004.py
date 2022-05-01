#urllib library
import urllib.error
import urllib.parse
import urllib.request

file = urllib.request.urlopen('http://data.pr4e.org/romeo.txt') #'': parse解析 the url 
#file: the urllib library return the web page looks like a file 
for line in file:  #read each line
    print(line.decode().strip())   #decode(): bytes strings to unicode strings
#*? then, we get the data from the web!!


#also can count in a dict
counts = dict()
for line in file:
    words = line.decode().split() 
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        