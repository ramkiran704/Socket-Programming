import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8080))

n = int(input("Enter the Size of Matrix (n): "))
print("Enter the 2 Matrices Row by Row:")

elements_1 = []
elements_2 = []
print("\nEnter Matrix 1:")
for i in range(n):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    elements_1.extend(row)

print("\nEnter Matrix 2:")
for i in range(n):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    elements_2.extend(row)

payload_list = [str(n)] + [str(x) for x in elements_1] + [str(x) for x in elements_2]
payload_str = " ".join(payload_list)

client.sendall(payload_str.encode())

response = client.recv(4096).decode()
result_matrix = list(map(int, response.split()))

print("\n--- Resultant Matrix (m3) ---")
for i in range(n):
    print(" ".join(map(str, result_matrix[i*n:(i+1)*n])))

client.close()