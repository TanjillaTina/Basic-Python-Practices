# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 20:56:54 2017
In The Name of Allah, The Beneficent and The Merciful
@author: TINA
"""

####Craeting a socket
"""
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect( ('data.pr4e.org', 80) )  ######(hostname,PortNumber)
print("Socket is Created")
"""
####What kind of Data I am going To send and receive (Application Protocol)

"""
##A simple web Browser using Python
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()


######
"""
##Getting UTF-8 o ASCII's
"""
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()



"""
##########
######Again creating a webBrowser Using "URLLIB"
"""
Since HTTP is so common,Python have a library that does all the socket work for us and makes web pages look like a file

"""

import urllib.request, urllib.parse, urllib.error

ffile = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in ffile:
    print(line.decode().strip())

#########
