import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",5000))
server.listen(1)
print("Server is Listening.........")
client_socket,client_address=server.accept()
print("Server is connected to :",client_address)
data=client_socket.recv(1024)
l=list(map(int,data.decode().split()))
n=len(l)
sum=0
for i in l:
    sum+=i
avg=sum/n

result="Sum is :"+str(sum)
result+="\nAvg is :"+str(avg)
client_socket.send(result.encode())