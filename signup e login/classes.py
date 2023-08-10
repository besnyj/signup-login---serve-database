import socket


class People:
    
    def __init__(self, name, age,  gender, email, password): # is working
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.password = password

    
    def register_new_user(): #is working
        
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect(('192.168.1.215', 35333))
        
        name = input("What is your name? ")
        age = int((input("What is your age? ")))
        gender = input("What is your gender? ")
        email = input("What is your email? ")
        password = input("Choose a password: ")

        info_package = ["Register", name, age, gender, email, password]
        result = ""
        for item in info_package:
            result += f'{item} '
        
        server.send(result.encode())
        response = server.recv(1024)
        response = response.decode()
        print(response)
        server.close()
        
    def check_user():
        
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect(('192.168.1.215', 35333))
        
        email = input("What is your email? ")
        password = input("Choose a password: ")

        info_package = ["Check", email, password]

        result = ""
        for item in info_package:
            result += f'{item} '

        server.send(result.encode())
        response = server.recv(1024)
        response = response.decode()
        print(response)
        server.close()
        
        