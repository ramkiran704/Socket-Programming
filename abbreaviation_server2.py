import socket
abb={
    "HTTP":"Hyper Text Transfer Protocol",
    "FTP":"File Transfer Protocol",
    "TCP":"Transmission Control Protocol",
    "UDP":"User Datagram Protocol"
}
server_socket=socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM
)
server_socket.bind(("0.0.0.0",6000))
print("Server is Listening.......")
print("Waiting for the Client Request")
while(True):
    data,address=server_socket.recvfrom(1024)
    req=data.decode().strip().upper()
    print("Request from :",address)
    res=abb.get(req,"Not Found")
    server_socket.sendto(res.encode(),address)