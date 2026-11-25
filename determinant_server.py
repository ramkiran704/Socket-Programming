import socket
import numpy as np
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 12345))
server.listen(1)
print("Server waiting for client...")
conn, addr = server.accept()
print("Client connected:", addr)

data = conn.recv(4096).decode()

values = list(map(int, data.split()))

n = values[0]
matrix = []

k = 1
for i in range(n):
    row = []
    for j in range(n):
        row.append(values[k])
        k += 1
    matrix.append(row)

det = round(np.linalg.det(matrix))

conn.sendall(str(det).encode())

print("Received Matrix:")
for row in matrix:
    print(row)

print("Determinant:", det)

conn.close()
server.close()
