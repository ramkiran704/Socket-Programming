import socket
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('127.0.0.1',5003))
while True:
    data,client_address=server.recvfrom(1024)
    message=data.decode()
    print("Message=",message)
    server.sendto("message received :".encode(),client_address)
