import sys
import dbops
import tkinter as tk
from datetime import datetime
note_id_list = []
selected = 0
# ======= FUNCTIONS ========
def onselect(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
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

def process_text():
    title = title_box.get()
    contents = text_box.get("1.0", tk.END)
    dbops.insert_note(dbops.conn, title, contents)

def delete_text():
    title_box.delete(0, tk.END)
    text_box.delete('1.0', tk.END)

def save_text():
    title = title_box.get()
    contents = text_box.get("1.0", tk.END)
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    dbops.update_note(dbops.conn, title, contents, selected, now)

def add_text(idx):
    note = dbops.select_specific_note(dbops.conn, idx)
    title_box.insert(0, note[0])
    text_box.insert('1.0', note[1])

# ======= USER INTERFACE ========
window = tk.Tk()
list_frame = tk.Frame()
content_frame = tk.Frame()
title_box = tk.Entry(master=content_frame)
text_box = tk.Text(master=content_frame)
list_box = tk.Listbox(master=list_frame)
# user message
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()
# test
title_box.pack()
text_box.pack()
list_box.pack()
list_box.bind('<<ListboxSelect>>', onselect)
update_list()
# buttons
add = tk.Button(master=list_frame, text="Add", command=process_text)
edit = tk.Button(master=list_frame, text="Save", command=save_text)
delete = tk.Button(master=list_frame, text="Delete", command=delete_text)
add.pack()
edit.pack()
delete.pack()
list_frame.pack(side=tk.LEFT)
content_frame.pack(side=tk.RIGHT)
window.mainloop()
def helloworld(out):
    out.write("Hello world of Python\n")


