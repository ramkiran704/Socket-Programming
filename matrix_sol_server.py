import socket
import ast
import threading

HOST = "127.0.0.1"
PORT = 5000


def handle_client(conn, addr):
    print("Client connected:", addr)

    data = conn.recv(4096).decode()
    matrix = ast.literal_eval(data)

    print("Matrix received from", addr)

    for row in matrix:
        print(row)

    n = len(matrix)

    upper = True
    lower = True
    diagonal = True

    for i in range(n):
        for j in range(n):

            if i > j and matrix[i][j] != 0:
                upper = False

            if i < j and matrix[i][j] != 0:
                lower = False

            if i != j and matrix[i][j] != 0:
                diagonal = False

    if diagonal:
        result = "Diagonal Matrix"
    elif upper:
        result = "Upper Triangular Matrix"
    elif lower:
        result = "Lower Triangular Matrix"
    else:
        result = "Neither Upper nor Lower Triangular Matrix"

    conn.send(result.encode())
    conn.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen(5)

print("Server started...")
print("Waiting for clients...")

while True:
    conn, addr = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(conn, addr)
    )

    thread.start()