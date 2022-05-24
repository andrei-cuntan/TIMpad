import sys
import dbops
import tkinter as tk


window = tk.Tk()
greeting = tk.Label(text="Hello, Tkinter")
button = tk.Button(
    text="Click me!",
    width=10,
    height=1,
    bg="cyan",
    fg="yellow",
)
entry = tk.Entry(fg="yellow", bg="blue", width=50)
text_box = tk.Text()
text_box.pack()
greeting.pack()
entry.pack()
button.pack()
window.mainloop()
def helloworld(out):
    out.write("Hello world of Python\n")


