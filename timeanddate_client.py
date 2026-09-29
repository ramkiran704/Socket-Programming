import socket
client_socket=socket.socket(
socket.AF_INET,
socket.SOCK_DGRAM
)
server_ip="127.0.0.1"
server_port=5000
client_socket.sendto(b"TIME",(server_ip,server_port))
data,address=client_socket.recvfrom(1024)
print("Time recevied from server:",data.decode())
client_socket.close()
