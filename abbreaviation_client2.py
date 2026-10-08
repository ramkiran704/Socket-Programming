import socket
client_socket=socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)
inp=input("Enter the Abbreaviation:")
client_socket.sendto(inp.encode(),("127.0.0.1",6000))
data,address=client_socket.recvfrom(1024)
print("Full Form of {inp} is :",data.decode())
client_socket.close()