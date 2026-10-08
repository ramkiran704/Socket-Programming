import socket
from datetime import datetime
server_socket=socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)
server_socket.bind(("0.0.0.0",5210))
print("Time Server is Running.....")
print("Waiting for Client.........")
while True:
    data,address=server_socket.recvfrom(1024)
    print("Requested from :",address)
    current_time=datetime.now().strftime("%Y-%m-%d : %M:%S")
    server_socket.sendto(current_time.encode(),address)