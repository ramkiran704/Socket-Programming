import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_ip = "127.0.0.1"
server_port = 5000
print("--- UDP Timezone Client ---")
print("Available examples: UTC, EST, PST, CST, IST, GMT, JST, CET, AEST")
requested_abbreviation = input("Enter timezone abbreviation: ").strip()
if requested_abbreviation:
 client_socket.sendto(requested_abbreviation.encode(), (server_ip, server_port))
 data, address = client_socket.recvfrom(1024)
 print("\nServer Response:", data.decode())
else:
 print("No abbreviation entered. Exiting.")
client_socket.close()
