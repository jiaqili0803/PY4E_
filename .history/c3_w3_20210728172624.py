import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #set a handle
mysock.connect(('data.pr4e.org', 80))  #set port
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()  
#GET; the webpage you want to get; need to encode
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')  #need to decode

mysock.close()

'''
就会得到
HTTP/1.1 200 OK
Date: Wed, 28 Jul 2021 09:01:17 GMT
Server: Apache/2.4.18 (Ubuntu)
Last-Modified: Sat, 13 May 2017 11:22:22 GMT
ETag: "1d3-54f6609240717"
Accept-Ranges: bytes
Content-Length: 467
Cache-Control: max-age=0, no-cache, no-store, must-revalidate
Pragma: no-cache
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Connection: close
Content-Type: text/plain
#below are contents
Why should you learn to write programs?

Writing programs (or programming) is a very creative
and rewarding activity.  You can write programs for
many reasons, ranging from making your living to solving
a difficult data analysis problem to having fun to helping
someone else solve a problem.  This book assumes that
everyone needs to know how to program, and that once
you know how to program you will figure out what you want
to do with your newfound skills.
'''
