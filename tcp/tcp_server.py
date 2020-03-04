import socket
import threading
import sys


TCP_IP = '127.0.0.1'
TCP_PORT = 5000
BUFFER_SIZE = 1024

def multiconnect(conn, addr):
    try:
        conn.settimeout(500)
        printed = False
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data: 
                # print('No data received.')
                break
            decoded_msg = data.decode()
            id, _ = decoded_msg.split(":")
            if printed == False:
                print("Connected Client:" + str(id) +'.')
                printed = True
            print(f"received data:{decoded_msg}")
            conn.send("pong".encode())
    except socket.timeout:
        print ('time out')
    conn.close()

def listen_forever():
    print("Server started at port: " + str(TCP_PORT))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    s.listen(3)

    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target = multiconnect, args=(conn, addr))
        thread.start()
listen_forever()
