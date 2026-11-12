import socket
server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("127.0.0.1",5010))
print("Server is Listening.......")
client_socket,client_address=server.recvfrom(1024)
value=client_socket.decode()
n=int(value)
sum=0
while n!=0:
    dig=n%10
    sum+=dig**3
    n=n//10
result=str(sum)
if result==value:
    result+="\t Armstrong"
else:
    result+="\t Not Armstrong"

server.sendto(result.encode(),client_address)
