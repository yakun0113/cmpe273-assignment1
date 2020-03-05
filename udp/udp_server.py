import socket
import select
import time
import sys

UDP_IP = "127.0.0.1"
IN_PORT = 5005
timeout = 3
data_ack = "ACKNOWLEDGEMENT"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, IN_PORT))
print("Server started at port 4000.")

while True:
	data, addr = sock.recvfrom(1024)
	print("Accepting a file upload...")
	if data:
		file_name = data.strip()

	f = open("server_received_data.txt", 'wb')
	# count = 0
	while True:
		ready = select.select([sock], [], [], timeout)
		if ready[0]:
			data, addr = sock.recvfrom(1024)
			# if count != 9995:
			sock.sendto(data_ack.encode(), addr)
			f.write(data)
			# count += 1
		else:
			print("Upload successfully completed." )
			f.close()
			break
