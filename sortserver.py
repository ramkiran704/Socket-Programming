import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('127.0.0.1',5000))
server.listen(1)
print("Server is listening.........")
client_socket,client_address=server.accept()

request=client_socket.recv(4096).decode()
array=list(map(int,request.split()))


# array.sort()
for i in range(len(array)-1):
    for j in range (len(array)-i-1):
        if array[j]>array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]

data="".join(map(str,array))
client_socket.sendall(data.encode())
