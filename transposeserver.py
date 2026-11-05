import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8081))
server.listen(1)

print("Transpose Server listening on port 8081...")
conn, addr = server.accept()

data = conn.recv(4096).decode()
parts = list(map(int, data.split()))

rows, cols = parts[0], parts[1]
elements = parts[2:]

matrix = [elements[i * cols:(i + 1) * cols] for i in range(rows)]

# Transpose computation
transpose = [[matrix[i][j] for i in range(rows)] for j in range(cols)]

# Prepare response as "cols rows val1 val2 ..."
result_elements = [val for row in transpose for val in row]
response = f"{cols} {rows} " + " ".join(map(str, result_elements))

conn.sendall(response.encode())
conn.close()
server.close()