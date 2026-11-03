import socket 
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while(True):
    message=input("ente message:")
    if message.lower()=="exit":
        break
    client.sendto(message.encode(),('127.0.0.1',5003))
    data,server_adress=client.recvfrom(1024)
    print(data.decode())
client.close()