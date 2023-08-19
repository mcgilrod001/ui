#imports sqlite3 and hashlib
import sqlite3
import hashlib
#initializes the database
conn = sqlite3.connect("userdata.db")
cur = conn.cursor()
#this is sql code inside of a multiline string it creates a table if one does not exsist that is called userdata
#it has 3 columns id, username, and password id is the primary key meaning it is auto incremented
#username and password are varcharts that cant be blank (NOT NULL)
cur.execute("""
    CREATE TABLE IF NOT EXISTS userdata ( 
        id INTEGER PRIMARY KEY, 
        username VARCHAR(255) NOT NULL, 
        password VARCHAR(255) NOT NULL
)
""")

#assighns username and password, encodes password wish sha256 through hashlib then hashes it.
username1, password1 = "user1", hashlib.sha256("pass1".encode()).hexdigest()
username2, password2 = "user2", hashlib.sha256("pass2".encode()).hexdigest()
username3, password3 = "user3", hashlib.sha256("pass3".encode()).hexdigest()
username4, password4 = "user4", hashlib.sha256("pass4".encode()).hexdigest()
#using cur.execute it runs the sql code to insert the username and password into the table under prepeared statements (the ?). the last tuple specifies that the username is the first ? and the password is the second ?
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username1, password1))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username2, password2))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username3, password3))
cur.execute("INSERT INTO userdata (username, password) VALUES (?, ?)", (username4, password4))
#commits the changes to the database
conn.commit()