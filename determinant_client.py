import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",12345))
n=int(input("Enter the number of row in Matrix:"))
print("Enter the Matrix:")
matrix=[]
for i in range(n):
    row=list(map(int,input(f"Row{i+1}:").split()))
    matrix.extend(row)
payload_list=[str(n)]+[str(x) for x in matrix]
payload_str=" ".join(payload_list)

client.sendall(payload_str.encode())

response=client.recv(4096).decode()
print("Determinant is :",response)