import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8082))
server.listen(1)

print("Scalar Multiplication Server listening on port 8082...")
conn, addr = server.accept()

data = conn.recv(4096).decode()
parts = list(map(int, data.split()))

k = parts[0]
rows, cols = parts[1], parts[2]
elements = parts[3:]

# Perform multiplication directly on flat list
result_elements = [val * k for val in elements]

# Format response: "rows cols val1 val2 ..."
response = f"{rows} {cols} " + " ".join(map(str, result_elements))

conn.sendall(response.encode())
conn.close()
server.close()