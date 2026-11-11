import socket 
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",5003))
server.listen(1)
print("Server is Listening......")

client_socket,client_address=server.accept()
request=client_socket.recv(4096).decode()
l=list(map(int,request.split()))
odd=[]
even=[]
prime=[]
for i in l:
    if i%2==1:
        odd.append(i)
    else:
        even.append(i)
    if i>1:
        is_prime=True
        for j in range(2,int(i**.5)+1):
            if i %j==0:
                is_prime=False
                break
        if is_prime:
            prime.append(i)
result="Odd NUmbers:"+ str(odd)
result+="\n Even Numbers:"+str(even)
result+="\n Prime Numbers:"+str(prime)

client_socket.sendall(result.encode())
