#imports sqlite3, hasklib, socket, and threading
#sqlite handles sql code and databeses
#haslib handles hashing and encrypting
#socket handles networking such as connecting to the server and sending data
import sqlite3
import hashlib
import socket
import threading
import rsa

#generates private and public keys each run
public_key, private_key = rsa.newkeys(1024)
#sets the  partner public key to none will be set later
public_partner = None


#sets the server up as a tcp server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sets the sertver to listen on port 9999 and sets the ip to localhost (set to private ip in production)
server.bind(("localhost", 9999))
#tells the server to listen for connections from laclalhost on port 9999 (tcp)
server.listen()

#remember to encrypt the password before sending it to the server, and encrypt connection
#defines a connection handler with the varibale c (c is the client)
def handle_connection(c):
    #sends the client an imput promt asking for username, encoded to bytes and encrypted with the client's public key
    c.send(rsa.encrypt("Username: ".encode(), public_partner))
    #recives the username from the client and decrypts it with the server's private key and decodes it
    username = rsa.decrypt(c.recv(1024), private_key).decode()
    #sends the client an imput promt asking for password, encodeed to bytes and encrypted with the client's public key
    c.send(rsa.encrypt("password: ".encode(), public_partner))
    #recives the password from the client and decrypts it with the server's private key and decodes it
    password = rsa.decrypt(c.recv(1024), private_key)
    #digests the password with sha256 though hashlib and hashes it
    password = hashlib.sha256(password).hexdigest()
    #connects to the database using sqlite3
    conn = sqlite3.connect("userdata.db")
    #sets a sql curson to cur for the database
    cur = conn.cursor()
    #runs sql code to select any valid entry on the table
    cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?", (username, password))
    #if the sql code renturns anyhting this is true and the login is successfull
    if cur.fetchall():
        #sends client a message saying login successful encoded to bytes and encrypted with the client's public key
        c.send(rsa.encrypt("login successful".encode(), public_partner))
        #this is the actual program you are granting access to
    #if nothing is valid nothing is returned and the lognin is not successfull
    else:
        #sends the client a message saying login failed, encoded to bytes, and encrypted with the client's public key
        c.send(rsa.encrypt("login failed".encode(), public_partner))
#while loop that auto accepts, and starts a thread for each connection
while True:
    #accepts the connection and sets the client and address to the variables client and addr
    client, addr = server.accept()
    #sends the client the server's public key
    client.send(public_key.save_pkcs1("PEM"))
    #recieves the client's public key
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
    #sets up a threat with the target of handling the conection with the argument client and starts the thread
    threading.Thread(target=handle_connection, args=(client,)).start()