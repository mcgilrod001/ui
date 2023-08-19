import socket
import rsa

#generates private and public keys each run
public_key, private_key = rsa.newkeys(1024)
#sets the  partner public key to none will be set later
public_partner = None

#sets the client up as a tcp client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to the server use public ip in client use private in server
client.connect(("localhost", 9999))

#recives the server's public key
public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
client.send(public_key.save_pkcs1("PEM"))
#recieves username prompt and decrypts it using private key of client and decodes it from bytes to string
message = rsa.decrypt(client.recv(1024), private_key).decode()
#sends username encrypted with server's public key and encoded to bytes
client.send(rsa.encrypt(input(message).encode(), public_partner))
#recieves password promt and decrypts it using private key of client and decodes it from bytes to string
message = rsa.decrypt(client.recv(1024), private_key).decode()
#sends password encrypted with server's public key and encoded to bytes
client.send(rsa.encrypt(input(message).encode(), public_partner))
#recieves login success or fail and decrypts it using private key of client and decodes it from bytes to string
print(rsa.decrypt(client.recv(1024), private_key).decode())
