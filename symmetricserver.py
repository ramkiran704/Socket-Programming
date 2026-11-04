import socket

# Create and configure socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8080))
server_socket.listen(1)

print("Server listening on port 8080...")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# Receive matrix dimension N
n = int(conn.recv(1024).decode())

# Receive matrix elements space-separated
data = conn.recv(1024).decode()
elements = list(map(int, data.split()))

# Reconstruct 2D matrix
matrix = [elements[i * n:(i + 1) * n] for i in range(n)]

# Classification logic
is_sym = True
is_diag = True
is_ident = True

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            is_sym = False
        if i != j and matrix[i][j] != 0:
            is_diag = False
        if i == j and matrix[i][j] != 1:
            is_ident = False
        if i != j and matrix[i][j] != 0:
            is_ident = False

if is_ident:
    result = "Identity Matrix"
elif is_diag:
    result = "Diagonal Matrix"
elif is_sym:
    result = "Symmetric Matrix"
else:
    result = "Neither Symmetric, Identity, nor Diagonal"

# Send result back
conn.sendall(result.encode())

conn.close()
server_socket.close()