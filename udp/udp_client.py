import socket
import time
import sys
import select

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
buf = 1024
timeout = 1
# file_name = sys.argv[1]
file_name = "upload.txt"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(file_name.encode(), (UDP_IP, UDP_PORT))
print("Connected to the server.")
print("Starting a file(upload.txt) upload...")

f = open(file_name, "r")
data = f.readline()
while(data):
    while True:
    	print("Received ack(" + data + ") from the server.")
    	sock.sendto(data.encode(), (UDP_IP, UDP_PORT))
    	ready = select.select([sock], [], [], timeout)
    	if ready[0]:
    		msg, addr = sock.recvfrom(1024)
    		if msg.decode() == "ACKNOWLEDGEMENT":
    			break
    
    data = f.readline()

sock.close()
f.close()
print("File upload successfully completed.")