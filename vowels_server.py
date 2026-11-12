import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('127.0.0.1',5000))
server.listen(1)
print("Server is Listening.......")

client_socket,client_address=server.accept()
vowels="aeiou"
word=client_socket.recv(1024).decode()
word=word.lower()
vowels_count=0
const_count=0
for i in word:
    if i.isalpha():
        if i in vowels:
            vowels_count+=1
        else:
            const_count+=1
result =f"Count Of Vowels : {vowels_count}"
result+=f"\nCount Of Consonants: {const_count}"
client_socket.send(result.encode())
    