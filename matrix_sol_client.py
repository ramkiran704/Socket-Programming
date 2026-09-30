import socket
HOST = "127.0.0.1"
PORT = 5000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
n = int(input("Enter matrix size: "))
matrix = []
print("Enter matrix:")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
    client.send(str(matrix).encode())
    result = client.recv(1024).decode()
    print("Result:", result)
    client.close()
