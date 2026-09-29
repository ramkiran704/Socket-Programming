import socket
from datetime import datetime
server_socket=socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)
server_socket.bind(("0.0.0.0",5000))
print("Time Server is running...")
print("Waiting for client request...")
while True:
    data,address=server_socket.recvfrom(1024)
    print("Request recevied from ",address)
    current_time=datetime.now().strftime("%Y-%m-%d:%M:%S")
    server_socket.sendto(current_time.encode(),address)