import socket

UDP_IP = ''
UDP_PORT = 36549

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP,UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    print("Received msg: ",data," from", addr)