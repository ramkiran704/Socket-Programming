import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8081))

rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))

elements = []
print(f"Enter the {rows}x{cols} matrix row by row (space-separated):")
for i in range(rows):
    row = list(map(int, input(f"Row {i + 1}: ").split()))
    elements.extend(row)

# Send format: "rows cols val1 val2 ..."
payload = f"{rows} {cols} " + " ".join(map(str, elements))
client.sendall(payload.encode())

data = client.recv(4096).decode()
parts = list(map(int, data.split()))

out_rows, out_cols = parts[0], parts[1]
res_elements = parts[2:]

print("\nTransposed Matrix from Server:")
for i in range(out_rows):
    print(" ".join(map(str, res_elements[i * out_cols:(i + 1) * out_cols])))

client.close()