import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8083))
server.listen(1)

print("Triangular Check Server listening on port 8083...")
conn, addr = server.accept()

data = conn.recv(4096).decode()
parts = list(map(int, data.split()))

n = parts[0]
elements = parts[1:]

matrix = [elements[i * n:(i + 1) * n] for i in range(n)]

is_upper = True
is_lower = True

for i in range(n):
    for j in range(n):
        if i > j and matrix[i][j] != 0:
            is_upper = False
        if i < j and matrix[i][j] != 0:
            is_lower = False

if is_upper and is_lower:
    result = "Diagonal Matrix"
elif is_upper:
    result = "Upper Triangular Matrix"
elif is_lower:
    result = "Lower Triangular Matrix"
else:
    result = "Neither Upper, Lower Triangular, nor Diagonal"

conn.sendall(result.encode())
conn.close()
server.close()