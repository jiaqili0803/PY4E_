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
