import socket

# Create socket and connect
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8080))

n = int(input("Enter matrix size N: "))
print(f"Enter the {n}x{n} matrix elements row by row (space-separated):")

elements = []
for i in range(n):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    elements.extend(row)

# Send dimension N first
client_socket.sendall(str(n).encode())
client_socket.recv(1024)  # Sync ack

# Send matrix elements
data_str = " ".join(map(str, elements))
client_socket.sendall(data_str.encode())

# Receive result from server
response = client_socket.recv(1024).decode()
print(f"\nServer Response: {response}")

client_socket.close()