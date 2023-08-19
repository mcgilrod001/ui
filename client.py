import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to the server use public ip in client use private in server
client.connect(("localhost", 9999))

message = client.recv(1024).decode()
client.send(input(message).encode())
message = client.recv(1024).decode()
client.send(input(message).encode())
print(client.recv(1024).decode())