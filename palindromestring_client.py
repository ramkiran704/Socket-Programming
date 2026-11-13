import socket
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s=input("Enter the string:")
client.sendto(s.encode(),("127.0.0.1",5000))
response,server_address=client.recvfrom(1024)
res=response.decode()
print(res)