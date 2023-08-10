import socket  ### IS WORKING.
import database

database.database_init()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.1.215', 35333))
server.listen()

while True:
    try:
        client, address = server.accept()
        request = client.recv(1024)
        request = request.decode() # request is what the main.py is asking for 
        request_info = request.split()

        if request_info[0] == "Register":
            database.register_user(name=request_info[1], age=request_info[2],
                                gender=request_info[3], email=request_info[4],
                                password=request_info[5])
            client.send("User registered in the database".encode())
        if request_info[0] == "Check":
            if database.check_user(email=request_info[1], password=request_info[2]) == 0:
                client.send("Access granted.".encode())
            if database.check_user(email=request_info[1], password=request_info[2]) == 1:
                client.send("Email/Password don't match.".encode())
            if database.check_user(email=request_info[1], password=request_info[2]) == 2:
                client.send("User does not exist".encode())
    except IndexError:
        pass