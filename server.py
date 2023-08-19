#imports sqlite3, hasklib, socket, and threading
#sqlite handles sql code and databeses
#haslib handles hashing and encrypting
#socket handles networking such as connecting to the server and sending data
import sqlite3
import hashlib
import socket
import threading

#sets the server up as a tcp server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#sets the sertver to listen on port 9999 and sets the ip to localhost (set to private ip in production)
server.bind(("localhost", 9999))
#tells the server to listen
server.listen()

#remember to encrypt the password before sending it to the server, and encrypt connection
#defines a connection handler with the varibale c (c is the client)
def handle_connection(c):
    #sends the client an imput promt asking for username, in encoded format so cumputer can understand
    c.send("Username: ".encode())
    # recieves the username from the client in 1024 byte chunks and decodes it so it is readable
    username = c.recv(1024).decode()
    #sends the client an imput promt asking for password, in encoded format so cumputer can understand (i need to encrypt this later so this is truly secure)
    c.send("password: ".encode())
    #recieves and decodes the client password (i need to encrypt this later so this is truly secure)
    password = c.recv(1024).decode()
    #digests the password with sha256 though hashlib and hashes it
    password = hashlib.sha256(password).hexdigest()
    #connects to the database using sqlite3
    conn = sqlite3.connect("userdata.db")
    #sets a sql curson to cur for the database
    cur = conn.cursor()
    #runs sql code to select any valid entry on the table
    cur.execute("SELECT * FROM userdata WHERE username = ? AND passsword = ?", (username, password))
    #if the sql code renturns anyhting this is true and the login is successfull
    if cur.fetchall():
        #sends the client a message saying login successful in encoded format to be readable by the computer
        c.send("login successful".encode())
        #this is the actual program you are granting access to
    #if nothing is valid nothing is returned and the lognin is not successfull
    else:
        #sends the client a message saying login failed in encoded format to be readable by the computer
        c.send("login failed".encode())
#while loop that auto accepts, and starts a thread for each connection
while True:
    #accepts the connection and sets the client and address to the variables client and addr
    client, addr = server.accept()
    #sets up a threat with the target of handling the conection with the argument client and starts the thread
    threading.Thread(target=handle_connection, args=(client,)).start()