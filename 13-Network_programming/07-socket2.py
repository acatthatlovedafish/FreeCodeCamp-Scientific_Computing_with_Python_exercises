# You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.

import socket

try:
    url = input("http://data.pr4e.org/intro-short.txt")
    split = url.split("/")
    host_name = split[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host_name, 80))
    cmd = f"GET {url} HTTP/1.0\r\n\r\n".encode()
    mysock.send(cmd)
except:
    print("Please enter a valid web address without www-s.")

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end = "")
mysock.close()
