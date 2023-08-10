import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


test_list = ["Check", "felipe@gmail.com", "1dasdadads"]

result = ""
for item in test_list:
    result += f'{item} '


server.connect(('192.168.1.215', 35353))
server.send(result.encode())
response = server.recv(1024)
response = response.decode()
print(response)


## IMPLEMENTAR CODIGO TESTE NA MAIN