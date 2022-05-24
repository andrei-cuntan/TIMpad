import sys
import dbops
import tkinter as tk
from datetime import datetime
note_id_list = []
selected = 0
# ======= FUNCTIONS ========

def onselect(evt):
    w = evt.widget
    try:
        index = int(w.curselection()[0])
    except IndexError:
        return
    delete_text()
    global selected
    selected = note_id_list[index]
    add_text(note_id_list[index])

def update_list():
    notelist = dbops.select_all_notes(dbops.conn)
    for idx, note in enumerate(notelist):
        list_box.insert(idx, note[2])
        if len(note_id_list) > idx:
            note_id_list[idx] = note[0]
        else:
            note_id_list.append(note[0])

def add_note():
    title = title_box.get()
    contents = text_box.get("1.0", tk.END)
    dbops.insert_note(dbops.conn, title, contents)
    status.config(text="Note added!")

def delete_text():
    title_box.delete(0, tk.END)
    text_box.delete('1.0', tk.END)

def save_note():
    title = title_box.get()
    contents = text_box.get("1.0", tk.END)
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    dbops.update_note(dbops.conn, title, contents, selected, now)
    status.config(text="Note saved!")

def add_text(idx):
    note = dbops.select_specific_note(dbops.conn, idx)
    title_box.insert(0, note[0])
    text_box.insert('1.0', note[1])

def delete_note():
    delete_text()
    dbops.delete_note(dbops.conn, selected)
    list_box.delete(0, tk.END)
    update_list()
    status.config(text="Note deleted!")
# ======= USER INTERFACE ========
window = tk.Tk()
list_frame = tk.Frame()
content_frame = tk.Frame()
greeting = tk.Label(text="Hello, Tkinter")
status = tk.Label(master=list_frame, text="")
title_box = tk.Entry(master=content_frame)
text_box = tk.Text(master=content_frame)
list_box = tk.Listbox(master=list_frame)
greeting.pack()
title_box.pack()
text_box.pack()
list_box.pack()
status.pack()
list_box.bind('<<ListboxSelect>>', onselect)
update_list()
# buttons
add = tk.Button(master=list_frame, text="Add", command=add_note)
edit = tk.Button(master=list_frame, text="Save", command=save_note)
delete = tk.Button(master=list_frame, text="Delete", command=delete_note)
add.pack()
edit.pack()
delete.pack()
list_frame.pack(side=tk.LEFT)
content_frame.pack(side=tk.RIGHT)
window.mainloop()
def helloworld(out):
    out.write("Hello world of Python\n")


