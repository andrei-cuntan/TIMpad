
import mysql.connector

conn = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="")

def create_db(conn):
    mycursor = conn.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS db_notes")

#invoke the function
#db_create_db(conn)
def create_table(conn):
    create_db(conn)
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS tb_notes (" \
            "note_id INT AUTO_INCREMENT PRIMARY KEY, " \
            "title VARCHAR(255) NOT NULL, " \
            "note VARCHAR(2000) NOT NULL)"
    mycursor.execute(query)


# invoking the function
#db_create_table(conn)
def insert_note(conn, title, note):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "INSERT INTO tb_notes (user_id, title, note) VALUES (1, %s, %s)"
    val = (title, note)
    mycursor.execute(query, val)
    conn.commit()
    return mycursor.lastrowid

records = [
        ('My first title', 'This is my first awesome note'),
        ('My second title', 'This is my second awesome note'),
        ('My third title', 'This is my third awesome note'),
        ('My fourth title', 'This is my fourth awesome note'),
        ('My fifth title', 'This is my fifth awesome note')
    ]

#for v in records:
    #db_insert_note(conn, v[0], v[1]) # invoke function
def select_all_notes(conn):
    conn.database = "db_notes"
    query = "SELECT * from tb_notes"
    mycursor = conn.cursor()
    mycursor.execute(query)
    return mycursor.fetchall()


def select_specific_note(conn, note_id):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    mycursor.execute("SELECT title, note FROM tb_notes WHERE note_id = " + str(note_id))
    return mycursor.fetchone()