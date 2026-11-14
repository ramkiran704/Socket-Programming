import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",5000))
server.listen(1)
print("Server is Listening.........")
client_socket,client_address=server.accept()
print("Server is connected to :",client_address)
data=client_socket.recv(1024)
l=list(map(int,data.decode().split()))
result="max Value is :"+str(max(l))
result+="\n Min value is :"+str(min(l))

client_socket.send(result.encode())
print(f"Response is send to the {client_address}")


