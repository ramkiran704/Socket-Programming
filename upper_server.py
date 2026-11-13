import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("127.0.0.1",12045))
server.listen(1)
print("Server is Listening.......")
client_socket,client_address=server.accept()
print(f"Server is Connected to {client_address}")
data=client_socket.recv(4096).decode()
if data:
    token=data.split()
    n=int(token[0])
    matrix_elements=list(map(int,token[1:1+n*n]))
    matrix=[matrix_elements[i*n:(i+1)*n] for i in range(n)]
    dia=True
    upper=True
    lower=True
    for i in range(n):
        for j in range(n):
            if i>j and matrix[i][j]!=0:
                upper=False
            if i<j and matrix[i][j]!=0:
                lower=False
            if i!=j and matrix[i][j]!=0:
                dia=False
    if dia:
        result="Diagonal"
    elif upper:
        result="Upper"
    elif lower:
        result="Lower"
    else:
        result="Nothing"
    client_socket.send(result.encode())
