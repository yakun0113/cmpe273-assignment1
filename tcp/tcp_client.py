import socket
import time
import sys


TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024
MESSAGE = "ping"
id= sys.argv[1]
delay = sys.argv[2]
number = sys.argv[3]


def send(id, delay, number):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    count = 0
    while True:
	    s.send(f"{id}:{MESSAGE}".encode())
	    print("Sending data: " + MESSAGE)
	    data = s.recv(BUFFER_SIZE)
	    print("Received data:", data.decode())
	    time.sleep(int(delay))
	    count += 1
	    if count >= int(number):
	    	break
    s.close()

send(id, delay, number)