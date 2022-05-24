import mysql.connector
conn = mysql.connector.connect(host="localhost", port=3306, user="root", passwd="")


def create_db(conn):
    mycursor = conn.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS db_notes")


def create_table(conn):
    create_db(conn)
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "CREATE TABLE IF NOT EXISTS tb_notes (" \
            "note_id INT AUTO_INCREMENT PRIMARY KEY, " \
            "title VARCHAR(255) NOT NULL, " \
            "note VARCHAR(2000) NOT NULL)"
    mycursor.execute(query)


def insert_note(conn, title, note):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "INSERT INTO tb_notes (user_id, title, note) VALUES (1, %s, %s)"
    val = (title, note)
    mycursor.execute(query, val)
    conn.commit()
    return mycursor.lastrowid


def update_note(conn, title, note, note_id, date):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    query = "UPDATE tb_notes SET title = %s, note = %s, timestamp = %s WHERE note_id = %s"
    val = (title, note, date, note_id)
    mycursor.execute(query, val)
    conn.commit()


def select_all_notes(conn):
    conn.database = "db_notes"
    query = "SELECT * from tb_notes"
    mycursor = conn.cursor()
    mycursor.execute(query)
    return mycursor.fetchall()


def select_specific_note(conn, note_id):
    conn.database = "db_notes"
    mycursor = conn.cursor()
    mycursor.execute("SELECT title, note , note_id FROM tb_notes WHERE note_id = " + str(note_id))
    return mycursor.fetchone()