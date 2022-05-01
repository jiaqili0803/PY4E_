#urllib library to get web data
import urllib.error
import urllib.parse
import urllib.request

file = urllib.request.urlopen('http://www.dr-chunk.com/page1.htm') 
#'': parse解析 the url 
#file: the urllib library return the web page looks like a file 
for line in file:  #read each line
    print(line.decode().strip())   #decode(): bytes strings to unicode strings
#*? then, we get the data from the web!!


#also can count words的出现频率 in a dict
counts = dict()
for line in file:
    words = line.decode().split() 
    #print(words)
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
        