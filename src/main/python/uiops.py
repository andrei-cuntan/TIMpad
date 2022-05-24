import tkinter as tk
import dbops

title_box = tk.Entry()
text_box = tk.Text()
list_box = tk.Listbox()
note_id_list = []

def onselect(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    delete_text()
    print(index, value)
    add_text(note_id_list[index])


list_box.bind('<<ListboxSelect>>', onselect)


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


def add_text(idx):
    note = dbops.select_specific_note(dbops.conn, idx)
    title_box.insert(0, note[0])
    text_box.insert('1.0', note[1])