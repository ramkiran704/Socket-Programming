import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8083))

n = int(input("Enter matrix size N: "))

elements = []
print(f"Enter the {n}x{n} matrix row by row (space-separated):")
for i in range(n):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    elements.extend(row)

# Format payload as: "N val1 val2 val3 ..."
payload = f"{n} " + " ".join(map(str, elements))
client.sendall(payload.encode())

response = client.recv(1024).decode()
print(f"\nServer Response: {response}")

client.close()