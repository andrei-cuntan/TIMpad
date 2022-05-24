import tkinter as tk
import dbops

title_box = tk.Entry()
text_box = tk.Text()

def process_text():
    title = title_box.get()
    contents = text_box.get("1.0", tk.END)
    dbops.insert_note(dbops.conn, title, contents)

def delete_text():
    title_box.delete(0, tk.END)
    text_box.delete('1.0', tk.END)