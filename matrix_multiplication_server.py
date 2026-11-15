import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(1)
print("Server listening on port 8080...")

client_socket, client_address = server.accept()
print(f"Connected to {client_address}")

data = client_socket.recv(4096).decode()

if data:
    tokens = data.split()
    print(f"Received tokens: {tokens}")
    
    n = int(tokens[0])

    m1_elements = list(map(int, tokens[1 : 1 + n*n]))
    m1 = [m1_elements[i*n : (i+1)*n] for i in range(n)]

    m2_elements = list(map(int, tokens[1 + n*n : 1 + 2*n*n]))
    m2 = [m2_elements[i*n : (i+1)*n] for i in range(n)]

    m3 = [[sum(m1[i][k] * m2[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

    m3_elements = [str(item) for row in m3 for item in row]
    m3_data = " ".join(m3_elements)
    
    client_socket.sendall(m3_data.encode())
    print("Result calculated and sent successfully!")

client_socket.close()
server.close()
print("Connection closed.")