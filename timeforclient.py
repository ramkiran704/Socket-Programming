import socket
client_socket=socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)

client_socket.sendto(b"TIME",("127.0.0.1",5210))
data,address=client_socket.recvfrom(1024)
print("Time recevied from server:",data.decode())
client_socket.close()