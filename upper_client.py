import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",12045))
n=int(input("Enter the number of rows:"))
matrix=[]
print("Enter teh matrix:")
for i in range(n):
    row=list(map(int,input("Enter Value").split()))
    matrix.extend(row) 
payload=[str(n)]+[str(x) for x in matrix]
payload_str=" ".join(payload)
client.sendall(payload_str.encode())
response=client.recv(4096)
result=response.decode()
print("result:",result)