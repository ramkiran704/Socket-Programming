import socket
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind(('127.0.0.1',5003))
server.listen(1)
print("Server is listening.........")
client_socket,client_address=server.accept()

request=client_socket.recv(1024).decode()
l=list(request)
result_list=[]
i=len(request)-1
while i >=0:
    result_list.append(l[i])
    i-=1

str1="".join(map(str,result_list))
result=str1
if (str1==request):
    result+="\tPalidrome"
else:
    result+="\tNot palindrome"
client_socket.send(result.encode())