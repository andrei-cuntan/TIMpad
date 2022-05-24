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
uiops.list_box.pack()
uiops.update_list()
# buttons
add = tk.Button(text="Add", command=uiops.process_text)
edit = tk.Button(text="Edit", command=uiops.add_text)
delete = tk.Button(text="Delete", command=uiops.delete_text)
add.pack()
edit.pack()
delete.pack()
window.mainloop()
def helloworld(out):
    out.write("Hello world of Python\n")


