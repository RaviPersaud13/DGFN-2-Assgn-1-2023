# Runs on PC, directly from Thonny
# The client

import socket
s = socket.socket()
host = '10.102.13.80' # #ip of raspberry pi, running the server
port = 5000
s.connect((host, port))
print(s.recv(1024))
s.close()
