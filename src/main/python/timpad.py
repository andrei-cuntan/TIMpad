import sys
import uiops
import dbops
import tkinter as tk


window = tk.Tk()
# user message
greeting = tk.Label(text="Hello, Tkinter")
greeting.pack()
# test

uiops.title_box.pack()
uiops.text_box.pack()
list_box = tk.Listbox()
list_box.pack()
notelist = dbops.select_all_notes(dbops.conn)
for note in notelist:
    print(note)
    list_box.insert(note[0], note[2])
# buttons
add = tk.Button(text="Add", command=uiops.process_text)
edit = tk.Button(text="Edit")
delete = tk.Button(text="Delete", command=uiops.delete_text)
add.pack()
edit.pack()
delete.pack()
window.mainloop()
def helloworld(out):
    out.write("Hello world of Python\n")


